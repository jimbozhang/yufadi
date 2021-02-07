# Yufadi

`Yufadi` is a toy project for Mandarin Grammar Error Correction (GEC) task. 

## Train

### Prepare the training text

The training text is required to be saved as `env/dataset/train-set`. It's format should be like the following example:

```plain
从 １ ９ ７ １ 年 开 始 计 划 生 育 ， 这 个 制 度 。	从 １ ９ ７ １ 年 开 始 执 行 计 划 生 育 这 个 制 度 。
然 后 我 去 上 学 ， 在 七 点 一 刻 。	我 上 学 是 在 七 点 一 刻 。
```

In this file, each line consists of a source sentence and a target sentence splited by a tab. 

All the charactors should be converted to full-width and be splited by a space.

Any charactors not in the vocabulary set (`resources/words.txt`) need to be replaced by the symbol "@".

### Run training

```bash
./train.sh
```

## Decode

### Check the model
Make sure the model directory contains the t2t model,
the vocab file and the `words.txt` file which maps the words into indexes.

An example:
```plain
env/models
└── transformer-transformer_base_single_gpu
    ├── checkpoint
    ├── events.out.tfevents.1579486340.speech-05-gpu
    ├── flags_t2t.txt
    ├── flags.txt
    ├── graph.pbtxt
    ├── hparams.json
    ├── model.ckpt-250000.data-00000-of-00002
    ├── model.ckpt-250000.data-00001-of-00002
    ├── model.ckpt-250000.index
    ├── model.ckpt-250000.meta
    ├── vocab.gec_problem.8192.subwords
    └── words.txt
```

### Process a local text file
```bash
python run_local_txt.py <model-path> <input-text>
```

### Run from a web browser
Start the server:
```bash
python start_server.py <model-path>
```
Then access http://0.0.0.0:1052 in your web browser.
