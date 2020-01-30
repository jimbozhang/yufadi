# yufadi-engine

Yufadi is a Mandarin Grammar Error Correction (GEC) engine. 

## Train

See `yufadi/train/run.sh`.


## Decode

### The model directory
The model directory should contain the t2t model,
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
python python run_local_txt.py <model-path> <input-text>
```

### Run in a web browser
Start the server:
```bash
./start_server.sh <model-path>
```
Then access http://0.0.0.0:1052 in your web browser.