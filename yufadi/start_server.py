# Copyright 2020 Junbo Zhang. All Rights Reserved.

import sys
from flask import Flask
import yufadi.wrapper as ygec

app = Flask(__name__)


@app.route('/')
def index():
    return 'Yufadi Demo.<p>例：<a href="http://0.0.0.0:1052/今天天气很冻。">http://0.0.0.0:1052/今天天气很冻。</a>'


@app.route('/<input_str>')
def url_input(input_str):
    output = 'Source: {}<p>Polished: {}'.format(input_str, processor(input_str))
    return output


if __name__ == "__main__":
    model_path = sys.argv[1]
    processor = ygec.Yufadi(model_path)
    app.run(host="0.0.0.0", port=1052)
