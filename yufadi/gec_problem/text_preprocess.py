# Copyright 2020 Junbo Zhang. All Rights Reserved.

import sys
import re


class SentencePreprocess:
    def __init__(self, model):
        self.unk_sym = '@'
        self.id_of_word = {}
        dict_fn = model + '/words.txt'
        with open(dict_fn) as f:
            for line in f:
                word, wid = re.split(r'\s+', line.strip('\n'))
                self.id_of_word[word] = wid

    @staticmethod
    def half2full_width(sen):
        # https://ramonyeung.github.io/2016/10/17/full-width-half-width-converting-Python
        full = ''
        for u in sen:
            num = ord(u)
            if num == 32:
                num = 0x3000
            elif 0x21 <= num <= 0x7E:
                num += 0xfee0
            u = chr(num)  # to unicode
            full += u
        return full

    @staticmethod
    def segment_by_char(sen):
        sen = re.sub(r'\s+', r'', sen)
        characters = [i for i in sen]
        return characters

    def oov2unk(self, sen):
        sen = self.half2full_width(sen)
        words = self.segment_by_char(sen)
        words_processed = []
        for w in words:
            if w not in self.id_of_word:
                if words_processed[-1] != self.unk_sym:
                    words_processed.append(self.unk_sym)
            else:
                words_processed.append(w)
        return ' '.join(words_processed)

    def __call__(self, *args, **kwargs):
        sen = args[0]
        sen = sen.strip('\n')
        return self.oov2unk(sen)


if __name__ == "__main__":
    dict_file = sys.argv[1] if len(sys.argv) >= 2 else 'words.txt'
    processor = SentencePreprocess(dict_file)
    for sen_src in sys.stdin:
        sen_tgt = processor(sen_src.strip('\n'))
        print(sen_tgt)
