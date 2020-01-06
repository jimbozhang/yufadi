# Copyright 2020 Junbo Zhang. All Rights Reserved.

# -*- coding: utf8 -*-


from yufadi import word_seg, gec


class Yufadi:
    def __init__(self):
        self.word_seg = word_seg.WordSeg()
        self.gec = gec.Gec()

    def run(self, sentence):
        # wordseg
        words = self.word_seg(sentence)

        # do correcting
        words_processed = self.gec(words)

        return ''.join(words_processed)
