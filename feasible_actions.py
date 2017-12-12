# -*- coding:utf8 -*-
def action_index(act_slot_response):
    """ Return the index of action """
    feasible_actions = [
        {'diaact': "request", 'inform_slots': {}, 'request_slots': {'child_name': 'UNK'}},
        {'diaact': "request", 'inform_slots': {}, 'request_slots': {'client_name': 'UNK'}},
        {'diaact': "request", 'inform_slots': {}, 'request_slots': {'phone_number': 'UNK'}},
        {'diaact': "request", 'inform_slots': {}, 'request_slots': {'child_age': 'UNK'}},
        {'diaact': "request", 'inform_slots': {}, 'request_slots': {'client_gender': 'UNK'}},
        {'diaact': "request", 'inform_slots': {}, 'request_slots': {'english_level': 'UNK'}},
        {'diaact': "request", 'inform_slots': {}, 'request_slots': {'client_location': 'UNK'}},
        {'diaact': "request", 'inform_slots': {}, 'request_slots': {'reserve_location': 'UNK'}},
        {'diaact': "request", 'inform_slots': {}, 'request_slots': {'reserve_time': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'fee': 'PLACEHOLDER'}, 'request_slots': {'child_name': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'teacher_nation': 'PLACEHOLDER'},
         'request_slots': {'child_name': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'online_course': 'PLACEHOLDER'}, 'request_slots': {'child_name': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'reserve_location': 'PLACEHOLDER'},
         'request_slots': {'phone_number': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'fee': 'PLACEHOLDER'}, 'request_slots': {'phone_number': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'teacher_nation': 'PLACEHOLDER'},
         'request_slots': {'phone_number': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'online_course': 'PLACEHOLDER'},
         'request_slots': {'phone_number': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'fee': 'PLACEHOLDER'}, 'request_slots': {'client_gender': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'fee': 'PLACEHOLDER'}, 'request_slots': {'child_age': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'online_course': 'PLACEHOLDER'},
         'request_slots': {'english_level': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'fee': 'PLACEHOLDER'}, 'request_slots': {'client_location': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'fee': 'PLACEHOLDER'}, 'request_slots': {'client_name': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'fee': 'PLACEHOLDER'}, 'request_slots': {'child_grade': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'class_type': 'PLACEHOLDER'}, 'request_slots': {'phone_number': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'fee': 'PLACEHOLDER'}, 'request_slots': {'english_level': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'school_location': 'PLACEHOLDER'},
         'request_slots': {'reserve_location': 'UNK'}},
        {'diaact': "request", 'inform_slots': {'fee': 'PLACEHOLDER'}, 'request_slots': {'client_location': 'UNK'}},

        {'diaact': "inform", 'inform_slots': {'fee': 'PLACEHOLDER'}, 'request_slots': {}},
        {'diaact': "inform", 'inform_slots': {'teacher_nation': 'PLACEHOLDER'}, 'request_slots': {}},
        {'diaact': "inform", 'inform_slots': {'online_course': 'PLACEHOLDER'}, 'request_slots': {}},
        {'diaact': "inform", 'inform_slots': {'school_location': 'PLACEHOLDER'}, 'request_slots': {}},
        {'diaact': "inform", 'inform_slots': {'class_type': 'PLACEHOLDER'}, 'request_slots': {}}
    ]
    if act_slot_response not in feasible_actions:
        feasible_actions.append(act_slot_response)
        print('补充action:', act_slot_response)
    for (i, action) in enumerate(feasible_actions):
        if act_slot_response == action:
            return i
action = {'diaact': "inform", 'inform_slots': {'school_location': 'PLACEHOLDER'}, 'request_slots': {}}
print(action_index(action))
