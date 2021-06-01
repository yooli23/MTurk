from random import choice
from flask import Flask, request, jsonify
import requests
import json
import sys

INSPIRED_CHATBOT_URL='http://interaction.cs.ucdavis.edu:3322/recommend_chatbot'
RAW_BLENDER_URL='http://dialog.cs.ucdavis.edu:6779/raw_blender'
INSPIRED_BASELINE_URL='http://language.cs.ucdavis.edu:7770/inspired_bot'

def init_model():
    return ['hello', 'how are you', 'whats up']


def speak(task_id, agent_name, context, user_utterance, model):

    # Finish task
    if agent_name == 'red':
        if len(context)-1 == 20:
            return "Task Finished!", True
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
                    'sid': task_id+"red",
                    'context': context,
                    'user_text': user_utterance,
                }
        try:
            resp = requests.post(
                        RAW_BLENDER_URL,
                        headers=headers,
                        data=json.dumps(data),
                        timeout=15)
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            print(e)
            return "CHATBOT ERROR! Sorry, please click 'complete chat'", True
        try:
            res = json.loads(resp.text)
            print(res)
        except:
            return "CHATBOT ERROR! Sorry, please click 'complete chat'", True
        if 'response' in res:
            response = res['response']
            end_chat = res['end_chat']
        return response, end_chat
    else:
        return "CHATBOT ERROR! Sorry, please click 'complete chat'", True

def typing_delay(utterance):    
    return min(100*len(utterance), 2000)


