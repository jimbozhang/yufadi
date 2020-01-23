from . import decoders


class LocalT2tDecoder(decoders.T2tDecoder):
    def __call__(self, sentence):
        return super().__call__(sentence)
