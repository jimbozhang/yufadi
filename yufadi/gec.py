# Copyright 2020 Junbo Zhang. All Rights Reserved.

# -*- coding: utf8 -*-

from yufadi import alt_word_generator
from yufadi import lm_beam_search


class Gec:
    def __init__(self):
        self.alt_word_generator = alt_word_generator.AltWordGenerator()
        self.lm_beam_search = lm_beam_search.LmBeamSearch()

    def make_alt_words(self, words):
        words_with_alts = []
        for w in words:
            alt_words = self.alt_word_generator(w)
            words_with_alts.append(alt_words)
        return words_with_alts

    def __call__(self, words):
        words_with_alts = self.make_alt_words(words)
        words_corrected = self.lm_beam_search(words_with_alts)
        return words_corrected
