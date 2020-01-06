# Copyright 2020 Junbo Zhang. All Rights Reserved.

import sys

from yufadi import yufadi


def run_one_sentence(sentence):
    return sentence + '\t' + yufadi.run(sentence)


def run_main():
    input_fn = sys.argv[1]

    engine = yufadi.Yufadi()
    with open(input_fn) as f:
        for line in f:
            print(engine.run(line.strip()))


if __name__ == "__main__":
    run_main()
