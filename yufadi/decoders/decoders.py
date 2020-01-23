import os, sys
import numpy as np
import tensorflow as tf
from tensor2tensor import models
from tensor2tensor import problems
from tensor2tensor.utils import trainer_lib
from tensor2tensor.utils import registry
from ..gec_problem import gec_problem


class T2tDecoder:
    def __init__(self, model_path):
        PROBLEM = 'gec_problem'
        DATA_DIR = model_path
        TRAIN_DIR = model_path
        MODEL = 'transformer'
        HPARAMS = 'transformer_base_single_gpu'

        self.tfe = tf.contrib.eager
        self.tfe.enable_eager_execution()
        Modes = tf.estimator.ModeKeys

        enfr_problem = problems.problem(PROBLEM)
        self.encoders = enfr_problem.feature_encoders(DATA_DIR)
        self.ckpt_path = tf.train.latest_checkpoint(os.path.join(TRAIN_DIR))

        hparams = trainer_lib.create_hparams(HPARAMS, data_dir=DATA_DIR, problem_name=PROBLEM)
        self.translate_model = registry.model(MODEL)(hparams, Modes.PREDICT)

    def translate(self, inputs):
        encoded_inputs = self.encode(inputs)
        with self.tfe.restore_variables_on_create(self.ckpt_path):
            model_output = self.translate_model.infer(encoded_inputs)['outputs']
        return self.decode(model_output)

    def encode(self, input_str, output_str=None):
        """Input str to features dict, ready for inference"""
        inputs = self.encoders['inputs'].encode(input_str) + [1]  # add EOS id
        batch_inputs = tf.reshape(inputs, [1, -1, 1])  # Make it 3D.
        return {'inputs': batch_inputs}

    def decode(self, integers):
        """List of ints to str"""
        integers = list(np.squeeze(integers))
        if 1 in integers:
            integers = integers[:integers.index(1)]
        return self.encoders["inputs"].decode(np.squeeze(integers))

    def __call__(self, sentence):
        return self.translate(sentence)
