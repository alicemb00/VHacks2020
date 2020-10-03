from flask import Flask, render_template, url_for, request, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import subprocess

import alpha
import golay
import rm

# UPLOAD_FOLDER = 'static'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/alphabetic', methods=['GET', 'POST'])
def alphabetic():
    if request.method == 'GET':
        try:
            return render_template('alphabetic.html', message="Enter your code (with spaces)")
        except:
            return 'There was a problem redirecting'
    else:
        return render_template('alphabetic.html', message="Output here")

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
            return render_template('golay.html', message="Enter your binary string here")
        except:
            return 'There was a problem redirecting'
    else:
        return render_template('golay.html', message="Output here")

@app.route('/binary/rm', methods=['GET', 'POST'])
def rm():
    if request.method == 'GET':
        try:
            return render_template('rm.html', message="Enter your binary string here")
        except:
            return 'There was a problem redirecting'
    else:
        return render_template('rm.html', message="Output here")

@app.route('/', methods=['GET'])
def upload_file():
    return render_template('home.html', message="Upload")

if __name__ == "__main__":
    app.run(debug=True)
