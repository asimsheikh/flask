from datetime import datetime
from typing import List
from uuid import uuid4, UUID

from pydantic import BaseModel
class Note(BaseModel):
    id: int
    uuid: UUID
    date: datetime
    text: str 
class JsonRepo:
    def __init__(self, name: str='JSON Repo'):
        self.name = name
        self.data = dict( id=1, name="Health", goals=[])
        self.notes: List[Note] = []

    def get_data(self):
        return self.data

    def add_goals(self, goal):
        self.data.get('goals').append(goal)

    def add_note(self, note: Note):
        self.notes.append(note)
        self.notes.sort(key=lambda note: note.date)
    
    def get_notes(self):
        return self.notes

    def clear(self):
        self.data = dict( id=1, name="Health", goals=[])

