from db import JsonRepo

data = dict(id=1, name="Health", goals=[])
data1 = dict(id=1, name="Health", goals=["30 mins gym everyday"])
data2 = dict(id=1, name="Health", 
             goals=["30 mins gym everyday",
                    "daily Muay Thai"])

def test_init():
    assert 2 == 2
    repo = JsonRepo()
    assert repo.get_data() == data

def test_add_goal():
    repo = JsonRepo()
    repo.add_goals("30 mins gym everyday")
    assert repo.get_data() == data1
    repo.add_goals("daily Muay Thai")
    assert repo.get_data() == data2

