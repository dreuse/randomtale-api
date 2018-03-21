from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')

@socketio.on('create')
def on_create(data):
    """Create a instance lobby"""
    inst = instance.Info(
        size=data['size'],
        teams=data['teams'],
        dictionary=data['dictionary'])
    room = inst.instance_id
    ROOMS[room] = inst
    join_room(room)
    emit('broad', {'room': room})

if __name__ == '__main__':
    socketio.run(app, debug=True)