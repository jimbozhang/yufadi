#!/usr/bin/env bash
# Copyright 2020 Junbo Zhang. All Rights Reserved.

stage=0

# User Config
ENV_DIR=env
TRAIN_SET=$ENV_DIR/dataset/train-set
DATA_DIR=$ENV_DIR/data
USR_DIR=yufadi/gec_problem
PROBLEM=gec_problem
MODEL=transformer
HPARAMS=transformer_base_single_gpu
OUTPUT_DIR=$ENV_DIR/models-new/$MODEL-$HPARAMS

# Activate Virtualenv
if [ ! -f venv/bin/python ]; then
  echo "venv not found."
  exit
fi
source venv/bin/activate

if [ $stage -le 0 ]; then
  # Data generate
  if [ ! -f $TRAIN_SET ]; then
    echo "Train set not found: $TRAIN_SET"
    exit
  fi
  TMP_DIR=$DATA_DIR/tmp
  mkdir -p $DATA_DIR $TMP_DIR
  cp $TRAIN_SET $DATA_DIR/train-set

  python venv/bin/t2t-datagen \
    --t2t_usr_dir=$USR_DIR \
    --data_dir=$DATA_DIR \
    --tmp_dir=$TMP_DIR \
    --problem=$PROBLEM
fi

if [ $stage -le 1 ]; then
  # Train
  mkdir -p $OUTPUT_DIR
  cp $DATA_DIR/vocab.gec_problem.*.subwords $OUTPUT_DIR
  cp resources/words.txt $OUTPUT_DIR

  python venv/bin/t2t-trainer \
    --t2t_usr_dir=$USR_DIR \
    --data_dir=$DATA_DIR \
    --problem=$PROBLEM \
    --model=$MODEL \
    --hparams_set=$HPARAMS \
    --output_dir=$OUTPUT_DIR
fi
