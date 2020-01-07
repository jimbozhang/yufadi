# Copyright 2020 Junbo Zhang. All Rights Reserved.

# -*- coding: utf8 -*-


class LmBeamSearch:
    def __init__(self):
        assert True

    @staticmethod
    def __call__(word_lists):
        result = []
        for slot in word_lists:
            result.append(slot[0])
        return result
