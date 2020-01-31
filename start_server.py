# Copyright 2020 Junbo Zhang. All Rights Reserved.

import sys

if len(sys.argv) < 2:
    print('Usage: python {} <model-path>'.format(sys.argv[0]))
    sys.exit()

import yufadi.server as server

model_path = sys.argv[1]
server.run(model_path)
