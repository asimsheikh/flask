from datetime import datetime 

data_1= { "id": 1, 
  "name": "Health", 
  "description": "The essense of health is being able to achieve all other life goals", 
  "goals": [
    "30 minutes gym every day",
    "daily muay thai", 
    "run 10km's at slow pace",
    "30 mins of stretching"
  ], 
  "notes": [
    dict(id=1,date=datetime(2022, 10, 6),note="Finding gym tough might need to diversify"),
    dict(id=2,date=datetime(2022, 10, 7),note="Working on improving my cardio levels"),
    dict(id=3,date=datetime(2022, 10, 8),note="Not sure how elementary to make things. Finding the tendons are creating too much damage"),
  ]}

data_2 = { "id": 2, 
  "name": "Business", 
  "description": "The ability to generate the monetary resources necessary to purse my dreams", 
  "goals": [
    "Build the alpha level of bloorocket in the crypto space",
    "Drive uber"
  ], 
  "notes": [
    dict(id=1,date=datetime(2022, 10, 6),note="Not much in the way of items to build out"),
    dict(id=2,date=datetime(2022, 10, 7),note="Noting that finding a place in the crypto space is hard"),
    dict(id=3,date=datetime(2022, 10, 9),note="Met with ethereum working group looking at learning"),
  ]}