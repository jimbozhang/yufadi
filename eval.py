# Copyright 2020 Junbo Zhang. All Rights Reserved.

import sys

from yufadi import yufadi


def run_main(v):
    model_path = sys.argv[1]
    input_fn = sys.argv[2]

    processor = yufadi.Yufadi(mode, model_path)
    with open(input_fn) as f:
        for line in f:
            result = processor(line)
            print('{} ---> {}'.format(line.strip('\n'), result))


if __name__ == "__main__":
    mode = 't2t-local'
    run_main(mode)
