# Copyright 2020 Junbo Zhang. All Rights Reserved.

import sys

if len(sys.argv) < 3:
    print('Usage: python {} <model-path> <input-text>'.format(sys.argv[0]))
    sys.exit()

import yufadi.wrapper as ygec

model_path = sys.argv[1]
input_fn = sys.argv[2]

processor = ygec.Yufadi(model_path)
with open(input_fn) as f:
    for line in f:
        result = processor(line)
        print('{} ---> {}'.format(line.strip('\n'), result))
