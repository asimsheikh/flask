class JsonRepo:
    def __init__(self, name='JSON Repo'):
        self.name = name
        self.data = dict( id=1, name="Health", goals=[])

    def get_data(self):
        return self.data

    def add_goals(self, goal):
        self.data.get('goals').append(goal)
    
    def clear(self):
        self.data = dict( id=1, name="Health", goals=[])

