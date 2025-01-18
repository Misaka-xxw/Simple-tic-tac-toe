import asyncio
import json
from flask import Flask, request, jsonify, send_file, redirect, send_from_directory, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
CORS(app)


# static resources
@app.route('/static/<filename>', methods=['GET'])
def get_static_files(filename):
    print(filename)
    STATIC_PATH = "./view/static"
    return send_from_directory(STATIC_PATH, filename)


@app.route('/css/<filename>', methods=['GET'])
def get_css(filename):
    print(filename)
    CSS_PATH = "./view/css"
    return send_from_directory(CSS_PATH, filename)


# redirect
@app.route('/', methods=['GET'])
def redirect2index():
    return redirect('/index.html')

@app.before_request
def redirect_before_request():
    if request.host == 'localhost:5000':
        return redirect('http://127.0.0.1:5000' + request.path, code=301)

@app.route('/<filename>', methods=['GET'])
def get_pages(filename):
    print(filename)
    return send_from_directory('./view', filename)


if __name__ == '__main__':
    app.run(debug=True)
