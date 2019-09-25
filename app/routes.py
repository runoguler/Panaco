from app import app
from flask import request

import os
from werkzeug.utils import secure_filename

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'


@app.route('/extract', methods = ['POST'])
def extract_info():
    if 'image' not in request.files:
        return {'Status': 404}
    data = request.files['image']
    if data.filename == '':
        return {'Status': 403}
    if data:
        filename = secure_filename(data.filename)
        data.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), filename))
        return {'Status': 200, 'Dosage': 2}
    else:
        return {'Status': 500}