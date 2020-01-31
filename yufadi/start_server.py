# Copyright 2020 Junbo Zhang. All Rights Reserved.

import sys
from flask import Flask, request, render_template, redirect
from wtforms import Form, StringField, validators, widgets
import yufadi.engine as ygec

app = Flask(__name__)


class InputForm(Form):
    input = StringField(
        label='',
        widget=widgets.TextArea(),
        validators=[
            validators.DataRequired(message=' '),
            validators.Length(max=100, message=u'当前版本，句子暂时不要超过100个汉字。对于段落的纠错，可以拆成句子多次运行。'),
        ],
        render_kw={'style':'font-size:12px;','class':'user'}
    )


def make_output(input_str):
    return render_template("result.html", input=input_str, result=gec_processor(input_str))


@app.route('/', methods=["GET", "POST"])
def home():
    form = InputForm(formdata=request.form)
    if request.method == "POST" and form.validate():
        return redirect('/{}'.format(form.data['input']))
    else:
        return render_template("input.html", form=form)


@app.route('/<input_str>')
def url_input(input_str):
    return make_output(input_str)


if __name__ == "__main__":
    model_path = sys.argv[1]
    gec_processor = ygec.Yufadi(model_path)
    app.run(host="0.0.0.0", port=1052)
