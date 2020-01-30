# Copyright 2020 Junbo Zhang. All Rights Reserved.

from yufadi.decoders.local_t2t_decoder import LocalT2tDecoder
from yufadi.gec_problem.text_preprocess import SentencePreprocess


class Yufadi:
    def __init__(self, model_path='.'):
        self.text_preprocessor = SentencePreprocess(model_path)
        self.predictor = LocalT2tDecoder(model_path)

    def __call__(self, sentence):
        sentence = self.text_preprocessor(sentence)
        return self.predictor(sentence).replace(' ', '')
