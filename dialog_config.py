sys_request_slots = ['moviename', 'theater', 'starttime', 'date', 'numberofpeople', 'genre', 'state', 'city', 'zip',
                     'critic_rating', 'mpaa_rating', 'distanceconstraints', 'video_format', 'theater_chain', 'price',
                     'actor', 'description', 'other', 'numberofkids']
sys_inform_slots = ['moviename', 'theater', 'starttime', 'date', 'genre', 'state', 'city', 'zip', 'critic_rating',
                    'mpaa_rating', 'distanceconstraints', 'video_format', 'theater_chain', 'price', 'actor',
                    'description', 'other', 'numberofkids', 'taskcomplete', 'ticket']

start_dia_acts = {
    # 'greeting':[],
    'request': ['moviename', 'starttime', 'theater', 'city', 'state', 'date', 'genre', 'ticket', 'numberofpeople']
}

################################################################################
# Dialog status
################################################################################
FAILED_DIALOG = -1
SUCCESS_DIALOG = 1
NO_OUTCOME_YET = 0

# Rewards
SUCCESS_REWARD = 50
FAILURE_REWARD = 0
PER_TURN_REWARD = 0

################################################################################
#  Special Slot Values
################################################################################
I_DO_NOT_CARE = "I do not care"
NO_VALUE_MATCH = "NO VALUE MATCHES!!!"
TICKET_AVAILABLE = 'Ticket Available'

################################################################################
#  Constraint Check
################################################################################
CONSTRAINT_CHECK_FAILURE = 0
CONSTRAINT_CHECK_SUCCESS = 1

################################################################################
#  NLG Beam Search
################################################################################
nlg_beam_size = 10

################################################################################
#  run_mode: 0 for dia-act; 1 for NL; 2 for no output
################################################################################
run_mode = 0
auto_suggest = 0

################################################################################
#   A Basic Set of Feasible actions to be Consdered By an RL agent
################################################################################
# feasible_actions = [
#     ############################################################################
#     #   greeting actions
#     ############################################################################
#     #{'diaact':"greeting", 'inform_slots':{}, 'request_slots':{}},
#     ############################################################################
#     #   confirm_question actions
#     ############################################################################
#     {'diaact':"confirm_question", 'inform_slots':{}, 'request_slots':{}},
#     ############################################################################
#     #   confirm_answer actions
#     ############################################################################
#     {'diaact': "confirm_answer", 'inform_slots': {}, 'request_slots': {}},
#     ############################################################################
#     #   thanks actions
#     ############################################################################
#     {'diaact': "thanks", 'inform_slots': {}, 'request_slots': {}},
#     ############################################################################
#     #   deny actions
#     ############################################################################
#     {'diaact': "deny", 'inform_slots': {}, 'request_slots': {}},
# ]
# ############################################################################
# #   Adding the inform actions
# ############################################################################
# for slot in sys_inform_slots:
#     feasible_actions.append({'diaact':'inform', 'inform_slots': {slot: "PLACEHOLDER"}, 'request_slots': {}})
#
# ############################################################################
# #   Adding the request actions
# ############################################################################
# for slot in sys_request_slots:
#     feasible_actions.append({'diaact': 'request', 'inform_slots': {}, 'request_slots': {slot: "UNK"}})

feasible_actions = [
    {'diaact': "greeting", 'inform_slots': {}, 'request_slots': {}},
    {'diaact': "bye", 'inform_slots': {}, 'request_slots': {}},
    {'diaact': 'request', 'request_slots': {'child_age': 'UNK'}, 'inform_slots': {}},
    {'diaact': 'request', 'request_slots': {'english_level': 'UNK'}, 'inform_slots': {}},
    {'diaact': 'request', 'request_slots': {'special_need': 'UNK'}, 'inform_slots': {'fee': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'},
     'inform_slots': {'special_need': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'},
     'inform_slots': {'ruisi_introduction': 'PLACEHOLDER'}},
    {'diaact': 'select', 'request_slots': {'reserve_location': 'UNK'},
     'inform_slots': {'reserve_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'}, 'inform_slots': {}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'}, 'inform_slots': {'class_length': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'}, 'inform_slots': {}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'}, 'inform_slots': {}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'},
     'inform_slots': {'attend_class_alone': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'special_need': 'UNK'}, 'inform_slots': {}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'},
     'inform_slots': {'allow_parents_together': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'}, 'inform_slots': {'class_type': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'}, 'inform_slots': {}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'}, 'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'},
     'inform_slots': {'allow_parents_together': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'},
     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'}, 'inform_slots': {}},
    {'diaact': 'request', 'request_slots': {'special_need': 'UNK'}, 'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'}, 'inform_slots': {'class_type': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'english_level': 'UNK'}, 'inform_slots': {'class_type': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'},
     'inform_slots': {'attend_class_alone': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'},
     'inform_slots': {'allow_parents_together': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'}, 'inform_slots': {'class_type': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'special_need': 'UNK'}, 'inform_slots': {'textbook': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'},
     'inform_slots': {'attend_class_alone': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'}, 'inform_slots': {'fee': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'english_level': 'UNK'}, 'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'english_level': 'UNK'},
     'inform_slots': {'allow_parents_together': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'},
     'inform_slots': {'attend_class_alone': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'}, 'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'}, 'inform_slots': {'fee': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'english_level': 'UNK'}, 'inform_slots': {'online_course': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'}, 'inform_slots': {'school_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'}, 'inform_slots': {'class_length': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'}, 'inform_slots': {'class_size': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'},
     'inform_slots': {'attend_class_alone': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'english_level': 'UNK'}, 'inform_slots': {'textbook': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'}, 'inform_slots': {'fee': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'}, 'inform_slots': {'textbook': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'},
     'inform_slots': {'school_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'}, 'inform_slots': {'class_length': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'}, 'inform_slots': {'online_course': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'special_need': 'UNK'}, 'inform_slots': {'class_type': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'},
     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}}, {'diaact': 'request', 'request_slots': {'special_need': 'UNK'},
                                                          'inform_slots': {'allow_parents_together': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'}, 'inform_slots': {'textbook': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'special_need': 'UNK'}, 'inform_slots': {'online_course': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'},
     'inform_slots': {'allow_parents_together': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'english_level': 'UNK'}, 'inform_slots': {'class_size': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'},
     'inform_slots': {'online_course': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'}, 'inform_slots': {'school_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'special_need': 'UNK'}, 'inform_slots': {'class_size': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'special_need': 'UNK'}, 'inform_slots': {'school_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'special_need': 'UNK'}, 'inform_slots': {'class_length': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'}, 'inform_slots': {'fee': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'}, 'inform_slots': {'textbook': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'}, 'inform_slots': {'class_length': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'english_level': 'UNK'}, 'inform_slots': {'class_length': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'}, 'inform_slots': {'textbook': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'}, 'inform_slots': {'fee': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'}, 'inform_slots': {'class_size': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'}, 'inform_slots': {'class_type': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'}, 'inform_slots': {'class_size': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'english_level': 'UNK'}, 'inform_slots': {'fee': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'english_level': 'UNK'},
     'inform_slots': {'attend_class_alone': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'},
     'inform_slots': {'class_length': 'PLACEHOLDER'}}, {'diaact': 'request', 'request_slots': {'english_level': 'UNK'},
                                                        'inform_slots': {'school_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'}, 'inform_slots': {'class_size': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'}, 'inform_slots': {'online_course': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'}, 'inform_slots': {'online_course': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'}, 'inform_slots': {'class_size': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'}, 'inform_slots': {'class_type': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'}, 'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'},
     'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'}, 'inform_slots': {'class_length': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'}, 'inform_slots': {'textbook': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'}, 'inform_slots': {'fee': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'},
     'inform_slots': {'class_length': 'PLACEHOLDER'}}, {'diaact': 'request', 'request_slots': {'client_name': 'UNK'},
                                                        'inform_slots': {'attend_class_alone': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'}, 'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'},
     'inform_slots': {'attend_class_alone': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'}, 'inform_slots': {'textbook': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'},
     'inform_slots': {'school_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'}, 'inform_slots': {'teacher_nation': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_name': 'UNK'}, 'inform_slots': {'school_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'child_name': 'UNK'}, 'inform_slots': {'class_size': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'},
     'inform_slots': {'allow_parents_together': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'}, 'inform_slots': {'online_course': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'special_need': 'UNK'},
     'inform_slots': {'attend_class_alone': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'}, 'inform_slots': {'class_size': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'},
     'inform_slots': {'school_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'},
     'inform_slots': {'allow_parents_together': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_time': 'UNK'}, 'inform_slots': {'school_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'}, 'inform_slots': {'textbook': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'},
     'inform_slots': {'online_course': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_gender': 'UNK'}, 'inform_slots': {'class_type': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'}, 'inform_slots': {'textbook': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'}, 'inform_slots': {'class_length': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'},
     'inform_slots': {'allow_parents_together': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'}, 'inform_slots': {'online_course': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'reserve_location': 'UNK'},
     'inform_slots': {'online_course': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'}, 'inform_slots': {'class_size': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'}, 'inform_slots': {'fee': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'}, 'inform_slots': {'class_type': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'client_location': 'UNK'},
     'inform_slots': {'attend_class_alone': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'phone_number': 'UNK'},
     'inform_slots': {'allow_parents_together': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'}, 'inform_slots': {'class_type': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'},
     'inform_slots': {'school_location': 'PLACEHOLDER'}},
    {'diaact': 'request', 'request_slots': {'know_about_ruisi': 'UNK'}, 'inform_slots': {'fee': 'PLACEHOLDER'}}]

act_set = {'request': 0, 'inform': 1, 'select': 2, "bye": 3, "greeting": 4}
slot_set = {
    "client_name": 0,
    "client_gender": 1,
    "child_name": 2,
    "child_age": 3,
    "child_grade": 4,
    "client_location": 5,
    "reserve_location": 6,
    "school_location": 7,
    "school_name": 8,
    "reserve_time": 9,
    "phone_number": 10,
    "school_phone": 11,
    "other_contact": 12,
    "sale": 13,
    "english_level": 14,
    "special_need": 15,
    "attend_class_before": 16,
    "know_about_ruisi": 17,
    "cut_in": 18,
    "user_goal": 19,
    "class_schedule": 20,
    "have_school_somewhere": 21,
    "attend_class_alone": 22,
    "allow_audition": 23,
    "audition_free": 24,
    "child_attend": 25,
    "allow_parents_together": 26,
    "person_accompany": 27,
    "class_length": 28,
    "audition_introduction": 29,
    "textbook": 30,
    "fulltime_or_sparetime": 31,
    "class_size": 32,
    "length_of_per_period": 33,
    "allow_return_premium": 34,
    "lesson_accompany": 35,
    "school_type": 36,
    "ruisi_introduction": 37,
    "teacher_nation": 38,
    "class_type": 39,
    "online_course": 40,
    "online_course_location": 41,
    "online_or_offline": 42,
    "fee": 43
}
