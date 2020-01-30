#!/usr/bin/env bash
# Copyright 2020 Junbo Zhang. All Rights Reserved.

. venv/bin/activate
export PYTHONPATH=$PYTHONPATH:./yufadi
python yufadi/start_server.py env/model/transformer-transformer_base_single_gpu
