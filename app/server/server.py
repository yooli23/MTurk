import os
import json
from threading import Timer

from flask import Flask, request, send_from_directory
from flask_socketio import SocketIO, emit, join_room

from utils.settings import Settings
from utils.server_utils import Task
from config.model import init_model, speak, typing_delay
from database.database import Database
from utils.bonus_utils import pay_bonus


# Init settings, model, db...
settings = Settings()
model = init_model()
database = Database()


# Init Server
app = Flask(__name__)
app.config['SECRET_KEY'] = settings.server_secret_key
socketio = SocketIO(app, logger=settings.logger, path=settings.server_socketio_path)


@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def root():
    return f"Welcome to {settings.task_name}."

@app.route('/<task_id>')
def task(task_id, methods=['GET', 'POST']):        
    task = Task(task_id, args=request.args)
    if task.user_accepted:
        database.init_task(task)
    return task.template

@socketio.on('register_user')
def register_user(data):
    task_id = data['task_id']
    join_room(task_id)

@socketio.on('request_model_utterance')
def send_model_utterance(data):
    # Extract data
    task_id = data['task_id']
    user_utterance = data['text']
    agent_name = data['agent_name']

    # Load context
    context = database.load_messages(task_id, agent_name)

    if context != []:
        context[-1]['human'] = user_utterance

    # Speak
    bot_utt, should_end_task = speak(task_id, agent_name, context, user_utterance, model)

    # Save messages
    database.save_message(task_id, agent_name, bot_utt, user_utterance)

    # End task condition
    if should_end_task:
        database.resign_agent(task_id, agent_name)        
        emit('agent_resigned', {'task_id': task_id, 'agent_name': agent_name}, room=task_id)

    # Send message
    emit('speak', {'task_id':task_id, 'agent_name': agent_name, 'text':bot_utt, 'typing_delay':typing_delay(bot_utt)}, room=task_id)    


@socketio.on('form_complete')
def save_form(data):
    task_id = data['task_id']
    title = data['title']
    result = data['form'].replace('"', '""').replace("'", "''")
    database.save_form(task_id, title, result)

@socketio.on('section_started')
def update_current_section(data):
    task_id = data['task_id']
    section_idx = data['section']
    database.update_task_section(task_id, section_idx)

@socketio.on('task_complete')
def mark_task_as_complete(data):    
    task_id = data['task_id']
    database.mark_task_as_complete(task_id)    
    t = Timer(150.0, pay_bonus, [task_id]) # changed from 30 second to 150 seconds
    t.start()
    emit('submit_mturk_form', {'task_id': task_id})