#!/usr/bin/env bash

cd "$(dirname "$0")"

set -e

rm -rf _virtualenv
virtualenv --python=`which python3` _virtualenv
. _virtualenv/bin/activate

# The advantage of using this method, in contrary to just calling `pip3 install -r requirements.txt` several times,
# is that it can detect different versions of the same dependency and fail with a "Double requirement given"
# error message.
pip3 install $(cat requirements.txt $(find lib -name requirements.txt | sort) | sort | uniq | sed 's/ *== */==/g')
