import os
from typing import Any
from flask import Flask, jsonify, request

from pydantic import BaseModel
from db import JsonRepo

class Action(BaseModel):
    type: str
    payload: dict[str, Any]

class AddPayload(BaseModel):
    goal: str

app = Flask(__name__)
repo = JsonRepo()

@app.route('/')
def index():
    return jsonify({"username": "Asim Sheikh"})

@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        action = Action(**request.json)
        payload = action.payload
        
        if action.type == 'GET_FOCUS':
            return repo.get_data()

        elif action.type == 'ADD_GOAL':
            payload = AddPayload(**action.payload)
            repo.add_goals(payload.goal)
            return {"ok": "True"}

        else:
            return {"ok": "False", "message": f"Not a valid action type {action.type}"}


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
