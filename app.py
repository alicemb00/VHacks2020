from flask import Flask, render_template, url_for, request, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import subprocess

import alpha
import golay as Golay
import rm as RM
import hamming as HAM
# import vingenre as Vingenre

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/alphabetic', methods=['GET', 'POST'])
def alphabetic():
    if request.method == 'GET':
        try:
            return render_template('alphabetic.html', message="Enter your encrypted text (with spaces) here!")
        except:
            return 'There was a problem redirecting'
    else:
        output = alpha.decrpyt_alpha(request.form['text'])
        return render_template('alphabetic.html', message=output[0], shift=output[1])

@app.route('/binary', methods=['GET', 'POST'])
def binary():
    try:
        return render_template('binary.html', message="Enter your binary string here")
    except:
        return 'There was a problem redirecting'


@app.route('/binary/golay', methods=['GET', 'POST'])
def golay():
    if request.method == 'GET':
        try:
            return render_template('golay.html', message="Enter your binary string of length 23 or 24 here!")
        except:
            return 'There was a problem redirecting'
    else:
        # if 'text' not in request.form or 'r' not in request.form or 'm' not in request.form:
        #    return render_template('golay.html', message="Please fill out all fields", error = "", codeword="")
        output = Golay.decode_golay(request.form['text'])
        return render_template('golay.html', message=output[2], error=output[0], codeword=output[1])

@app.route('/binary/ham', methods=['GET', 'POST'])
def ham():
    if request.method == 'GET':
        try:
            return render_template('ham.html', message="Enter your binary string of length 23 or 24 here!")
        except:
            return 'There was a problem redirecting'
    else:
        # if 'text' not in request.form or 'r' not in request.form or 'm' not in request.form:
        #    return render_template('golay.html', message="Please fill out all fields", error = "", codeword="")
        output = HAM.correct_hamming(request.form['text'])
        return render_template('ham.html', message=output[2], error=output[0], codeword=output[1])

@app.route('/binary/rm', methods=['GET', 'POST'])
def rm():
    if request.method == 'GET':
        try:
            return render_template('rm.html', message="Enter your binary string, r value, and m value here!")
        except:
            return 'There was a problem redirecting'
    else:
        output = RM.decode_rm(request.form['text'], request.form['r'], request.form['m'])
        return render_template('rm.html', message=output[1], error=output[0])
"""
@app.route('/alphabetic/vingenre', methods=['GET', 'POST'])
def vingenre():
    if request.method == 'GET':
        try:
            return render_template('vingenre.html', message="")
        except:
            return 'There was a problem redirecting'
    else:
        output = Vingenre.decode_vingenre(request.form['text'])
        return render_template('vingenre.html', message=output)

@app.route('/alphabetic/other', methods=['GET', 'POST'])
def other():
    if request.method == 'GET':
        try:
            return render_template('other.html', message="")
        except:
            return 'There was a problem redirecting'
    else:
        output = alpha.decrpyt_alpha(request.form['text'])
        return render_template('other.html', message=output)
"""
@app.route('/', methods=['GET'])
def upload_file():
    return render_template('home.html', message="Upload")

if __name__ == "__main__":
    app.run(debug=True)
