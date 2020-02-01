# Copyright 2020 Junbo Zhang. All Rights Reserved.

import re

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.utils import registry


@registry.register_problem
class GecProblem(text_problems.Text2TextProblem):
    """Grammar Error Correction problem for T2T."""

    @property
    def approx_vocab_size(self):
        return 2 ** 13  # ~8k

    @property
    def is_generate_per_split(self):
        # generate_data will shard the data into TRAIN and EVAL for us.
        return False

    @property
    def dataset_splits(self):
        """Splits of data to produce and number of output shards for each."""
        # 10% evaluation data
        return [{
            "split": problem.DatasetSplit.TRAIN,
            "shards": 9999,
        }, {
            "split": problem.DatasetSplit.EVAL,
            "shards": 1,
        }]

    def generate_samples(self, data_dir, tmp_dir, dataset_split):
        del tmp_dir
        del dataset_split

        data_file = data_dir + '/train-set'

        with open(data_file, encoding='utf-8') as f:
            for line in f:
                items = re.split(r'\t', line.strip('\n'))
                if len(items) != 2:
                    continue
                if items[1] == '0':
                    continue

                yield {
                    "inputs": items[0],
                    "targets": items[1]
                }
