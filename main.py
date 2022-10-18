from __future__ import annotations
from datetime import datetime 

import os
import random  
from uuid import uuid4

from typing import Any, Dict
from flask import Flask, jsonify, request
from flask_cors import CORS

from pydantic import BaseModel
from db import JsonRepo, Note

from faker import Faker

class Action(BaseModel):
    name: str
    payload: Dict[str, Any]

class AddPayload(BaseModel):
    goal: str

class AddNotePayload(BaseModel):
    date: str 
    text: str

app = Flask(__name__)
CORS(app)
repo = JsonRepo()

faker = Faker()

def parse_js_date(js_date_string: str) -> datetime:
    return datetime.strptime(js_date_string, '%a, %d %b %Y %H:%M:%S GMT')

@app.route('/')
def index():
    return jsonify({"username": "Asim Sheikh"})

@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        action = Action(**request.json)
        payload = action.payload

        print(action)
        
        if action.name== 'GET_FOCUS':
            return repo.get_data()

        elif action.name== 'ADD_GOAL':
            payload = AddPayload(**payload)
            repo.add_goals(payload.goal)
            return {"ok": True }

        elif action.name == 'CLEAR_FOCUS':
            repo.clear()
            return {"ok": True}

        elif action.name == 'ADD_NOTE':
            payload = AddNotePayload(**payload)
            note = Note(id=random.randint(a=1,b=10000),
                        uuid=uuid4(), 
                        date=parse_js_date(payload.date),
                        text=payload.text)
            repo.add_note(note)
            return {"ok": True}

        elif action.name == 'GET_NOTES':
            return repo.get_notes()

        else:
            return {"ok": "False", "message": f"Not a valid action type {action.name}"}


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
