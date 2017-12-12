# Created by Helic on 2017/7/27

from agent_dqn import *

params = {
    'experience_replay_pool_size': 10000,
    'dqn_hidden_size': 60,
    'gamma': 0.9,
    'predict_mode': True,
    'max_turn': 40,
    'trained_model_path': 'data/saved_model_10000.p'
}

agent_dqn = AgentDQN(params)  # 初始化参数需要改
state_example = {
    'user_action': {'diaact': 'inform', 'request_slots': {}, 'inform_slots': {'user_goal': '预约'}, 'speaker': 'user',
                    'turn': 0},
    'current_slots': {'inform_slots': {'user_goal': '预约'}, 'request_slots': {}, 'proposed_slots': {},
                      'agent_request_slots': {}}, 'turn': 1, 'history': [
        {'diaact': 'inform', 'request_slots': {}, 'inform_slots': {'user_goal': '预约'}, 'speaker': 'user', 'turn': 0}],
    'agent_action': {'diaact': 'greeting', 'inform_slots': {}, 'request_slots': {}}}

with open("data/result_for_test.json", 'r', encoding='utf-8') as f:
    value = json.load(f)
    for i in value:
        print("user:       ", value[i][0]["user_action"])
        pre_index = agent_dqn.dqn.predict(agent_dqn.prepare_state_representation(value[i][0]), {'activation_func': 'relu'})
        pre_agent_action = agent_dqn.index_to_action(pre_index)
        print("prediction: ", pre_agent_action)
        print("label:      ", value[str(int(i)+1)][0]["agent_action"])
        print("********************************************************************************************\n")
