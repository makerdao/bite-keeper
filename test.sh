#!/bin/sh

PYTHONPATH=$PYTHONPATH:./lib/pymaker py.test --cov=bite_keeper --cov-report=term --cov-append tests/
