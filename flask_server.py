import asyncio
import json
from flask import Flask, request, jsonify, send_file, redirect, send_from_directory, session
from flask_cors import CORS

from Algorithm import Algorithm

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
CORS(app)
client_ip=None
board=Algorithm()

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

@app.route('/css/fonts/<filename>', methods=['GET'])
def get_fonts(filename):
    print(filename)
    CSS_PATH = "./view/css/fonts"
    return send_from_directory(CSS_PATH, filename)

# redirect
@app.route('/', methods=['GET'])
def redirect2index():
    client_ip = request.remote_addr
    return redirect('/index.html')

@app.before_request
def redirect_before_request():
    if request.host == 'localhost:5000':
        return redirect('http://127.0.0.1:5000' + request.path, code=301)

@app.route('/<filename>', methods=['GET'])
def get_pages(filename):
    global client_ip
    print(filename)
    return send_from_directory('./view', filename)

@app.route('/api/drop', methods=['POST'])
async def drop():
    if request.content_type != 'application/json':
        return jsonify({"error": "Content type must be application/json",
                        "status": "error"}), 400
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({"message": "Invalid JSON", "status": "error"}), 400
    player_id=data.get("player_id")
    auto=data.get("auto")
    mode=data.get("mode")
    if auto==0: # 不是机器第一步
        chess_id = data.get("chess_id")
        board.play_step(player_id,auto=False,x=chess_id/3,y=chess_id%3)
        if mode==1:
            board.play_step(3-player_id)


if __name__ == '__main__':
    app.run(debug=True)
