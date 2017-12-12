
from state_tracker import StateTracker
from user_simulator import UserSimulator
from agent_dqn import AgentDQN

params = {
    'experience_replay_pool_size': 10000,
    'dqn_hidden_size': 60,
    'gamma': 0.9,
    'predict_mode': True,
    'max_turn': 40,
    'trained_model_path': 'data/saved_model.p'
}

state_tracker = StateTracker()
usersim = UserSimulator(3)
agent = AgentDQN(params)


def run_episode(count):
    for i in range(count):
        print("dialog:", i)
        episode_over = False
        turn = 0
        state_tracker.initialize_episode()
        agent_action = {'diaact': 'greeting', 'inform_slots': {}, 'request_slots': {}}
        state_tracker.update(agent_action=agent_action)
        print("sys:", agent_action)
        user_action = {'diaact': 'inform', 'inform_slots': {'user_goal': 'ԤԼ'}, 'request_slots': {}}
        state_tracker.update(user_action=user_action)
        print("user:", user_action)
        turn += 2
        while not episode_over:
            state = state_tracker.get_state()
            # print("state:", state['current_slots'])
            agent_action = agent.dqn.predict(agent.prepare_state_representation(state), {'activation_func': 'relu'})
            agent_action = agent.index_to_action(agent_action)
            state_tracker.update(agent_action=agent_action)
            print("sys:", agent_action)
            user_action = usersim.user_response(agent_action)
            state_tracker.update(user_action=user_action)
            print("user:", user_action)
            turn += 2
            if user_action['diaact'] == 'bye' or turn > 38:
                episode_over = True
            else:
                episode_over = False

run_episode(1)


