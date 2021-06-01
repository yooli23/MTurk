from random import choice
from flask import Flask, request, jsonify
import requests
import json
import sys

RAW_BLENDER_URL='http://dialog.cs.ucdavis.edu:6779/raw_blender'

headers = {
            'Content-Type': 'application/json',
}
data = {
            'sid': "acedd"+"red",
            'context': ['hello', 'how are you', 'whats up'],
            'user_text': "hello",
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
    print("CHATBOT ERROR! Sorry, please click 'complete chat'")
try:
    res = json.loads(resp.text)
    print(res)
except:
    print("CHATBOT ERROR! Sorry, please click 'complete chat'")