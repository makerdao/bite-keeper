# bite-keeper

![Build Status](https://github.com/makerdao/bite-keeper/actions/workflows/.github/workflows/tests.yaml/badge.svg?branch=master)
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

### Installation
#### Prerequisites
- [Python v3.6.6](https://www.python.org/downloads/release/python-366/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
    - This project requires *virtualenv* to be installed if you want to use Maker's python tools. This helps with making sure that you are running the right version of python and checks that all of the pip packages that are installed in the **install.sh** are in the right place and have the right versions.

In order to clone the project and install required third-party packages please execute:
```
git clone https://github.com/makerdao/bite-keeper.git
cd bite-keeper
git submodule update --init --recursive
./install.sh
```

For some known Ubuntu and macOS issues see the [pymaker](https://github.com/makerdao/pymaker) README.

## Usage

```
usage: bite-keeper [-h] [--rpc-host RPC_HOST] [--rpc-timeout RPC_TIMEOUT]
                   --eth-from ETH_FROM [--eth-key KEYFILE_STRING]
                   --tub-address TUB_ADDRESS [--graphql-url GRAPHQL_URL]
                   [--gas-price GAS_PRICE] [--bitecdps-address BITECDPS_ADDRESS]
                   [--top] [--chunks] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  --rpc-host RPC_HOST   JSON-RPC host (default: `http://localhost:8545')
  --rpc-timeout RPC_TIMEOUT
                        JSON-RPC timeout (in seconds, default: 10)
  --eth-from ETH_FROM   Ethereum account from which to send transactions
  --eth-key KEYFILE_STRING
                        path to keyfile (key_file=./k.json,pass_file=./p.txt")
  --tub-address TUB_ADDRESS
                        Ethereum address of the Tub contract
  --graphql-url GRAPHQL_URL
                        GraphQL URL (default: https://sai-mainnet.makerfoundation.com/v1)
  --bitecdps-address BITECDPS_ADDRESS
                        Ethereum address of the BiteCdps contract
  --gas-price GAS_PRICE
                        Gas price in Wei (default: node default)
  --top                 Only bite the top N cups (default: 500)
  --chunks              Only bite N cups at a time (default: 100)
  --debug               Enable debug output
```

## License

See [COPYING](https://github.com/makerdao/bite-keeper/blob/master/COPYING) file.

### Disclaimer

YOU (MEANING ANY INDIVIDUAL OR ENTITY ACCESSING, USING OR BOTH THE SOFTWARE INCLUDED IN THIS GITHUB REPOSITORY) EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE SOFTWARE IS AT YOUR SOLE RISK.
THE SOFTWARE IN THIS GITHUB REPOSITORY IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
YOU RELEASE AUTHORS OR COPYRIGHT HOLDERS FROM ALL LIABILITY FOR YOU HAVING ACQUIRED OR NOT ACQUIRED CONTENT IN THIS GITHUB REPOSITORY. THE AUTHORS OR COPYRIGHT HOLDERS MAKE NO REPRESENTATIONS CONCERNING ANY CONTENT CONTAINED IN OR ACCESSED THROUGH THE SERVICE, AND THE AUTHORS OR COPYRIGHT HOLDERS WILL NOT BE RESPONSIBLE OR LIABLE FOR THE ACCURACY, COPYRIGHT COMPLIANCE, LEGALITY OR DECENCY OF MATERIAL CONTAINED IN OR ACCESSED THROUGH THIS GITHUB REPOSITORY.
