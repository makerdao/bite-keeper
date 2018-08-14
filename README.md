# bite-keeper

[![Build Status](https://travis-ci.org/makerdao/bite-keeper.svg?branch=master)](https://travis-ci.org/makerdao/bite-keeper)
[![codecov](https://codecov.io/gh/makerdao/bite-keeper/branch/master/graph/badge.svg)](https://codecov.io/gh/makerdao/bite-keeper)

The _DAI Stablecoin System_ incentivizes external agents, called _keepers_,
to automate certain operations around the Ethereum blockchain.

`bite-keeper` is one of the simplest keepers. It constantly monitors a `Tub` contract
looking for unsafe cups and bites them the moment they become unsafe. Ultimately,
it should take into account the profit it can make by processing the resulting
collateral via `bust` and only waste gas on `bite` if it can make it up by
subsequent arbitrage. For now, it is a dumb keeper that just bites every cup
that can be bitten.

<https://chat.makerdao.com/channel/keeper>

## Installation

This project uses *Python 3.6.2*.

In order to clone the project and install required third-party packages please execute:
```
apt-get build-essential automake pkg-config libtool libffi-dev libgmp-dev python-dev libsecp256k1-dev
git clone https://github.com/makerdao/bite-keeper.git
cd bite-keeper
git submodule update --init --recursive
pip3 install -r requirements.txt
```

For some known macOS issues see the [pymaker](https://github.com/makerdao/pymaker) README.

## Usage

```
usage: bite-keeper [-h] [--rpc-host RPC_HOST] [--rpc-port RPC_PORT]
                   [--rpc-timeout RPC_TIMEOUT] --eth-from ETH_FROM
                   --tub-address TUB_ADDRESS [--gas-price GAS_PRICE] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  --rpc-host RPC_HOST   JSON-RPC host (default: `localhost')
  --rpc-port RPC_PORT   JSON-RPC port (default: `8545')
  --rpc-timeout RPC_TIMEOUT
                        JSON-RPC timeout (in seconds, default: 10)
  --eth-from ETH_FROM   Ethereum account from which to send transactions
  --tub-address TUB_ADDRESS
                        Ethereum address of the Tub contract
  --gas-price GAS_PRICE
                        Gas price in Wei (default: node default)
  --debug               Enable debug output
```

## License

See [COPYING](https://github.com/makerdao/bite-keeper/blob/master/COPYING) file.

### Disclaimer

YOU (MEANING ANY INDIVIDUAL OR ENTITY ACCESSING, USING OR BOTH THE SOFTWARE INCLUDED IN THIS GITHUB REPOSITORY) EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE SOFTWARE IS AT YOUR SOLE RISK.
THE SOFTWARE IN THIS GITHUB REPOSITORY IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
YOU RELEASE AUTHORS OR COPYRIGHT HOLDERS FROM ALL LIABILITY FOR YOU HAVING ACQUIRED OR NOT ACQUIRED CONTENT IN THIS GITHUB REPOSITORY. THE AUTHORS OR COPYRIGHT HOLDERS MAKE NO REPRESENTATIONS CONCERNING ANY CONTENT CONTAINED IN OR ACCESSED THROUGH THE SERVICE, AND THE AUTHORS OR COPYRIGHT HOLDERS WILL NOT BE RESPONSIBLE OR LIABLE FOR THE ACCURACY, COPYRIGHT COMPLIANCE, LEGALITY OR DECENCY OF MATERIAL CONTAINED IN OR ACCESSED THROUGH THIS GITHUB REPOSITORY. 
