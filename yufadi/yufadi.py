# Copyright 2020 Junbo Zhang. All Rights Reserved.

# -*- coding: utf8 -*-


from yufadi.decoders.local_t2t_decoder import LocalT2tDecoder
from yufadi.gec_problem.text_preprocess import SentencePreprocess


class Yufadi:
    def __init__(self, mode='t2t-local', model_path='.'):
        self.mode = mode
        self.run_functions = {
            't2t-local': self.run_mode_t2t_local,
            't2t-client': self.run_mode_t2t_client
        }
        assert self.mode in self.run_functions

        self.text_preprocessor = SentencePreprocess(model_path)

        if mode == 't2t-local':
            self.predictor = LocalT2tDecoder(model_path)
        else:
            assert False

    def run_mode_t2t_local(self, sentence):
        sentence = self.text_preprocessor(sentence)
        return self.predictor(sentence)

    @staticmethod
    def run_mode_t2t_client(self, sentence):
        return sentence

    def __call__(self, sentence):
        return self.run_functions[self.mode](sentence)
