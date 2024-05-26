from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

rooms = {}  # Room name to key mapping
user_rooms = {}  # Username to list of rooms mapping

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        if username:
            session['username'] = username
            if username not in user_rooms:
                user_rooms[username] = []
            return redirect(url_for('dashboard'))
    return render_template('home.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))
    username = session['username']
    return render_template('dashboard.html', username=username, rooms=user_rooms[username])

@app.route('/create', methods=['POST'])
def create_room():
    room = request.form['room']
    key = request.form['key']
    username = session.get('username')
    if room not in rooms:
        rooms[room] = key
        user_rooms[username].append(room)
        return jsonify(success=True, room=room)
    return jsonify(success=False, error="Room already exists.")

@app.route('/join', methods=['POST'])
def join_room_route():
    room = request.form['room']
    key = request.form['key']
    username = session.get('username')
    if room in rooms and rooms[room] == key:
        user_rooms[username].append(room)
        return jsonify(success=True, room=room)
    return jsonify(success=False, error="Incorrect room or key.")

@app.route('/delete', methods=['POST'])
def delete_room():
    room = request.form['room']
    username = session.get('username')
    if room in user_rooms[username]:
        user_rooms[username].remove(room)
        if not any(room in rooms_list for rooms_list in user_rooms.values()):
            del rooms[room]
        return jsonify(success=True)
    return jsonify(success=False, error="Room not found in your list.")

@app.route('/chat/<room>')
def chat(room):
    if 'username' not in session or room not in user_rooms[session['username']]:
        return redirect(url_for('dashboard'))
    username = session['username']
    return render_template('chat.html', username=username, room=room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    msg = data['msg']
    username = session.get('username')
    if username and room:
        full_msg = f"{username}: {msg}"
        send(full_msg, to=room)
    

@socketio.on('join')
def on_join(data):
    room = data['room']
    username = session.get('username')
    if username and room:
        join_room(room)
        send(f"{username} has joined the room.", to=room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    username = session.get('username')
    if username and room:
        leave_room(room)
        send(f"{username} has left the room.", to=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
