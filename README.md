# DQN_fewer_slots

## Current Slots and Acts
```python
act_set = {'request': 0, 'inform': 1, "bye": 2, "greeting": 3, "select": 4}
slot_set = {
    "client_name": 0,
    "client_gender": 1,
    "child_age": 2,
    "english_level": 3,
    "client_location": 4,
    "reserve_location": 5,  
    "reserve_time": 6,
    "phone_number": 7,
    "user_goal": 8,
    "fee": 9,
    "teacher_nation": 10
}

sys_request_slots = ["child_age", "client_location", "reserve_location", "phone_number",
                     "client_name", "client_gender", "reserve_time", "user_goal"]
sys_inform_slots = ['teacher_nation', 'fee']
```

## Current Feasible Actions
```python
feasible_actions = [{'diaact': 'greeting', 'inform_slots': {}, 'request_slots': {}},
                    {'diaact': 'bye', 'inform_slots': {}, 'request_slots': {}},
                    {'diaact': 'request', 'request_slots': {'child_age': 'UNK'}, 'inform_slots': {}},
                    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'}, 'inform_slots': {}},
                    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'}, 'inform_slots': {}},
                    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'}, 'inform_slots': {}},
                    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'}, 'inform_slots': {}},
                    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'}, 'inform_slots': {}},
                    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'}, 'inform_slots': {}},
                    {'diaact': 'request', 'request_slots': {'user_goal': 'UNK'}, 'inform_slots': {}},
                    {'diaact': 'inform', 'request_slots': {}, 'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
                    {'diaact': 'inform', 'request_slots': {}, 'inform_slots': {'fee': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'child_age': 'UNK'},
                     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'child_age': 'UNK'},
                     'inform_slots': {'fee': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'},
                     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'},
                     'inform_slots': {'fee': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'},
                     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'},
                     'inform_slots': {'fee': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'},
                     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'},
                     'inform_slots': {'fee': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'},
                     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'},
                     'inform_slots': {'fee': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'},
                     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'},
                     'inform_slots': {'fee': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'},
                     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'},
                     'inform_slots': {'fee': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'user_goal': 'UNK'},
                     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
                    {'diaact': 'request', 'request_slots': {'user_goal': 'UNK'},
                     'inform_slots': {'fee': 'PLACEHOLDER'}},
                     {'diaact': 'select', 'request_slots': {'reserve_location': 'UNK'},
                     'inform_slots': {'reserve_location': 'PLACEHOLDER'}}
                     ]
```
