# Copyright 2020 Junbo Zhang. All Rights Reserved.

# -*- coding: utf8 -*-


class Gec:
    def __init__(self):
        assert True

    @staticmethod
    def __call__(words):
        words_corrected = words
        words_corrected.append('</s>')
        return words_corrected
