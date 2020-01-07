# Copyright 2020 Junbo Zhang. All Rights Reserved.

# -*- coding: utf8 -*-

import synonyms


class AltWordGenerator:
    def __init__(self):
        assert True

    @staticmethod
    def __call__(word):
        result = synonyms.nearby(word)
        result = result[0]
        result.append(word)
        return result


if __name__ == "__main__":
    engine = AltWordGenerator()
    print(engine('恳求'))
    print(engine('要求'))
    print(engine('我'))
