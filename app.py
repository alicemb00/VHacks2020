from flask import Flask, render_template, url_for, request, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import subprocess

# UPLOAD_FOLDER = 'static'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/alphabetic', methods=['GET', 'POST'])
def troubleshootFailed():
    if request.method == 'GET':
        try:
            return render_template('alphabetic.html', message="Enter your code (with spaces)")
        except:
            return 'There was a problem redirecting'
    else:
        return render_template('alphabetic.html', message="Output here")

@app.route('/binary')
def troubleshootQuality():
    try:
        return render_template('binary.html')
    except:
        return 'There was a problem redirecting'


@app.route('/', methods=['GET'])
def upload_file():
    return render_template('home.html', message="Upload")

if __name__ == "__main__":
    app.run(debug=True)
