# This file is part of Maker Keeper Framework.
#
# Copyright (C) 2017 reverendus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest

from bite_keeper.bite_keeper import BiteKeeper
from pymaker.feed import DSValue
from pymaker.numeric import Wad
from pymaker.deployment import Deployment
from tests.helper import args, captured_output


class TestBiteKeeper:
    def test_should_not_start_without_eth_from_argument(self, deployment: Deployment):
        # when
        with captured_output() as (out, err):
            with pytest.raises(SystemExit):
                BiteKeeper(args=args(f""), web3=deployment.web3)

        # then
        assert "error: the following arguments are required: --eth-from" in err.getvalue()

    def test_should_not_start_without_tub_address_argument(self, deployment: Deployment):
        # when
        with captured_output() as (out, err):
            with pytest.raises(SystemExit):
                BiteKeeper(args=args(f"--eth-from {deployment.web3.eth.defaultAccount}"), web3=deployment.web3)

        # then
        assert "error: the following arguments are required: --tub-address" in err.getvalue()

    def test_should_bite_unsafe_cups_only(self, deployment: Deployment):
        # given
        keeper = BiteKeeper(args=args(f"--eth-from {deployment.web3.eth.defaultAccount} --tub-address {deployment.tub.address}"),
                            web3=deployment.web3)

        # and
        deployment.tub.join(Wad.from_number(10)).transact()
        deployment.tub.mold_cap(Wad.from_number(100000)).transact()
        DSValue(web3=deployment.web3, address=deployment.tub.pip()).poke_with_int(Wad.from_number(250).value).transact()

        # and
        deployment.tub.open().transact()
        deployment.tub.lock(1, Wad.from_number(4)).transact()
        deployment.tub.draw(1, Wad.from_number(1000)).transact()

        # and
        assert deployment.tub.safe(1)

        # when
        keeper.check_all_cups()

        # then
        assert deployment.tub.safe(1)
        assert deployment.tub.tab(1) == Wad.from_number(1000)

        # when
        DSValue(web3=deployment.web3, address=deployment.tub.pip()).poke_with_int(Wad.from_number(150).value).transact()

        # and
        assert not deployment.tub.safe(1)

        # and
        keeper.check_all_cups()

        # then
        assert deployment.tub.safe(1)
        assert deployment.tub.tab(1) == Wad.from_number(0)

    @staticmethod
    def prepare_unsafe_cup(deployment: Deployment):
        deployment.tub.join(Wad.from_number(10)).transact()
        deployment.tub.mold_cap(Wad.from_number(100000)).transact()
        DSValue(web3=deployment.web3, address=deployment.tub.pip()).poke_with_int(Wad.from_number(250).value).transact()

        deployment.tub.open().transact()
        deployment.tub.lock(1, Wad.from_number(4)).transact()
        deployment.tub.draw(1, Wad.from_number(1000)).transact()

        # price goes down, the cup becomes unsafe
        DSValue(web3=deployment.web3, address=deployment.tub.pip()).poke_with_int(Wad.from_number(150).value).transact()

    @staticmethod
    def used_gas_price(deployment):
        return deployment.web3.eth.getBlock('latest', full_transactions=True).transactions[0].gasPrice

    def test_should_use_default_gas_price_by_default(self, deployment: Deployment):
        # given
        keeper = BiteKeeper(args=args(f"--eth-from {deployment.web3.eth.defaultAccount} --tub-address {deployment.tub.address}"),
                            web3=deployment.web3)

        # and
        self.prepare_unsafe_cup(deployment)

        # when
        keeper.check_all_cups()

        # then
        assert self.used_gas_price(deployment) == deployment.web3.eth.gasPrice

    def test_should_use_fixed_gas_price_if_asked_to_go_so(self, deployment: Deployment):
        # given
        keeper = BiteKeeper(args=args(f"--eth-from {deployment.web3.eth.defaultAccount} --tub-address {deployment.tub.address} "
                                      f"--gas-price 129000000000"),
                            web3=deployment.web3)

        # and
        self.prepare_unsafe_cup(deployment)

        # when
        keeper.check_all_cups()

        # then
        assert self.used_gas_price(deployment) == 129000000000
