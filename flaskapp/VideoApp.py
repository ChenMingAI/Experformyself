from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import time
app = Flask(__name__)
socketio = SocketIO(app)

now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

@app.route("/")
def hello():
    return render_template('localapp.html')
@app.route("/ping")
def test():
    return "pong"
@app.route("/getImage")
def getImage():
    return render_template("show.html")

@socketio.on('my other event', namespace='/test')
def test_message(message):
    print("get data..", message['data'])
    type(message['data'])
    emit('video response', {'data': message['data']} ,broadcast=True)

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=5000)