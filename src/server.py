from translator import *
from time import time
from flask import Flask, flash, g, redirect, render_template, request, session, url_for
import sys, re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mainHandler():
    if request.method == "GET":
        return render_template('main.html')

    elif request.method == "POST":
        mode = request.form["mode"]
        method = request.form["method"]
        text = request.form["text"]

@app.route('/result', methods=['POST'])
def showResult():
    mode = request
    return render_template('result.html')