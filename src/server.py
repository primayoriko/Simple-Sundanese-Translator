from translator import *
from time import time
from flask import Flask, flash, g, redirect, render_template, request, session, url_for
import sys, re, os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mainHandler():
    if request.method == "GET":
        return render_template('main.html', initInput="", result="")

    elif request.method == "POST":
        translator = Translator(indoDict="data/indonesia.txt", sundaDict="data/sunda.txt")
        mode = request.form["mode"]
        method = request.form["method"]
        text = request.form["text"]
        tehOpt = request.form.get("tehOpt")
        # print(mode + ' ' + method + ' ' + text)
        # print('getcwd:      ', os.getcwd())
        # print('__file__:    ', __file__)
        return render_template('main.html', initInput=text, result=\
                translator.setText(text).translate(mode, method, tehOpt=="yes"))