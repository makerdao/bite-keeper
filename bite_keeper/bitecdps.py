# This file is part of the Maker Keeper Framework.
#
# Copyright (C) 2020 Maker Foundation
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

from datetime import datetime
from web3 import Web3
from typing import List

from pymaker import Address, Contract, Transact
from pymaker.util import int_to_bytes32

class BiteCdps(Contract):
    """A client for the `BiteCdps` contract, which houses logic that makes
        changes to the Maker Protocol.

    You can find the source code of the `BiteCdps` contract here:
        https://github.com/makerdao/bite-cdps/blob/master/src/BiteCdps.sol

    Attributes:
        web3: An instance of `Web` from `web3.py`.
        address: Ethereum address of the `BiteCdps` contract.
    """

    abi = Contract._load_abi(__name__, 'abi/BiteCdps.abi')
    bin = Contract._load_bin(__name__, 'abi/BiteCdps.bin')

    def __init__(self, web3: Web3, address: Address):
        assert (isinstance(web3, Web3))
        assert (isinstance(address, Address))

        self.web3 = web3
        self.address = address
        self._contract = self._get_contract(web3, self.abi, address)

    @staticmethod
    def deploy(web3: Web3, tubAddress: Address):
        return BiteCdps(
            web3=web3,
            address=Contract._deploy(
                web3, BiteCdps.abi, BiteCdps.bin, [tubAddress.address]
            )
        )

    def bite(self, cdps: List):
        bytes32CDPs = []
        for cdp in cdps:
            bytes32CDPs.append(int_to_bytes32(cdp))

        return Transact(
            self,
            self.web3,
            self.abi,
            self.address,
            self._contract,
            'bite(bytes32[])',
            [bytes32CDPs]
        )
