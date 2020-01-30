#!/usr/bin/env bash
# Copyright 2020 Junbo Zhang. All Rights Reserved.

if [ $# != 1 ]; then
   echo "usage: start_server <model-dir>"
   exit 1;
fi

MODEL=$1

. venv/bin/activate
export PYTHONPATH=$PYTHONPATH:./yufadi
python yufadi/start_server.py "$MODEL"
