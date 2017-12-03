# bite-keeper

[![Build Status](https://travis-ci.org/makerdao/bite-keeper.svg?branch=master)](https://travis-ci.org/makerdao/bite-keeper)
[![codecov](https://codecov.io/gh/makerdao/bite-keeper/branch/master/graph/badge.svg)](https://codecov.io/gh/makerdao/bite-keeper)
[![Maintainability](https://api.codeclimate.com/v1/badges/b6026b4e21fca450d860/maintainability)](https://codeclimate.com/github/makerdao/bite-keeper/maintainability)

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
git clone https://github.com/makerdao/bite-keeper.git
git submodule update --init --recursive
pip3 install -r requirements.txt
```

### Known macOS issues

In order for the Python requirements to install correctly on _macOS_, please install
`openssl`, `libtool` and `pkg-config` using [Homebrew](https://brew.sh/):
```
brew install openssl libtool pkg-config
```

and set the `LDFLAGS` environment variable before you run `pip3 install -r requirements.txt`:
```
export LDFLAGS="-L$(brew --prefix openssl)/lib" CFLAGS="-I$(brew --prefix openssl)/include" 
```

## Usage

```
usage: bite-keeper [-h] [--rpc-host RPC_HOST] [--rpc-port RPC_PORT] --eth-from
                   ETH_FROM --tub-address TUB_ADDRESS [--gas-price GAS_PRICE]
                   [--debug] [--trace]

optional arguments:
  -h, --help            show this help message and exit
  --rpc-host RPC_HOST   JSON-RPC host (default: `localhost')
  --rpc-port RPC_PORT   JSON-RPC port (default: `8545')
  --eth-from ETH_FROM   Ethereum account from which to send transactions
  --tub-address TUB_ADDRESS
                        Ethereum address of the Tub contract
  --gas-price GAS_PRICE
                        Gas price in Wei (default: node default)
  --debug               Enable debug output
  --trace               Enable trace output
```

## License

See [COPYING](https://github.com/makerdao/keeper/blob/master/COPYING) file.
