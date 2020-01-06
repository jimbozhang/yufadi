# Copyright 2020 Junbo Zhang. All Rights Reserved.

# -*- coding: utf8 -*-

import jieba


class WordSeg:
    def __init__(self):
        jieba.initialize()

    @staticmethod
    def __call__(sentence):
        words = jieba.cut(sentence)
        words = list(words)
        return words
