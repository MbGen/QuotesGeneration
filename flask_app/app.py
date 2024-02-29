from flask import Flask, render_template
from flask_socketio import SocketIO

from model import generate

app = Flask(__name__)

app.secret_key = 'randomsecretkeyfordebugging'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('json')
def handle_message(data):
    start_word = data['msg']

    generated_text = generate(start_word, length=100)

    json_ = {
        'msg': generated_text 
    }

    socketio.emit('json', json_)


if __name__ == '__main__':
    socketio.run(app, host="localhost", port=5000, allow_unsafe_werkzeug=True)
