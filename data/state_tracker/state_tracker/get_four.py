# transform data to state
# data = [[{diaact:'', inform_slots:{}, request_slots:{}, speaker: '', 'turn':''}, {}, {}],[],[]]
# state = {'agent_action':None, 'user_action':None, 'turn':0, 'history':[],
# 'current_slots':{'agent_request_slots':{}, 'inform_slots':{}, 'proposed_slots':{},
# 'request_slots':{}}}

import json
import operator
from state_tracker import StateTracker


class GetFour:
    def __init__(self, path):
        with open(path) as f:
            self.data = json.load(f)
        self.tracker = StateTracker()
        self.four = {}  # output result
        self.index = 0  # the index of output
        self.feasible_action = {0:{'diaact': 'greeting', 'inform_slots': {}, 'request_slots': {}}, 1:{'diaact': 'bye', 'inform_slots':{}, 'request_slots':{}}}
        self.feasible_action_index = 2

    def init_episode(self):
        self.num_turns = 0  # the number of turns for a episode
        self.tracker.initialize_episode()
        self.episode_over = False
        self.reward = 0
        self.a_s_r_over_history = []  # action_state pairs history
        self.action = {}  # the action now
        self.state = {}
        self.episode_status = -1


    def get_a_s_r_over(self, episode_record):   # episode_record = [{},{},{}
        self.init_episode()
        self.num_turns = len(episode_record)
        for i in range(len(episode_record)):
            self.action = episode_record[i]
            a_s_r_over = {"3": False}
            if self.action["speaker"] == "agent":
                self.state = self.tracker.get_state()
                self.tracker.update(agent_action=self.action)
                self.reward += self.reward_function(self.episode_status)
                a_s_r_over["0"] = self.action
                self.action_index(self.action)
                a_s_r_over["1"] = self.state
                a_s_r_over["2"] = self.reward
                if a_s_r_over["1"]['agent_action'] == None:
                    a_s_r_over["1"]['agent_action'] = {'diaact': 'greeting', 'inform_slots':{}, 'request_slots':{}}
                self.a_s_r_over_history.append(a_s_r_over)
            else:
                self.tracker.update(user_action=self.action)
                self.reward += self.reward_function(self.episode_status)
                if i == self.num_turns:
                    self.a_s_r["0"] = 0
                    self.a_s_r["1"] = self.state
                    self.a_s_r["2"] = self.reward
                    self.a_s_r_over_history.append(self.a_s_r)
        # when dialog over, update the latest reward
        self.episode_status = self.get_status(self.a_s_r_over_history[-1]["1"])
        self.reward += self.reward_function(self.episode_status)
        self.a_s_r_over_history[-2]["2"] = self.reward
        self.a_s_r_over_history[-2]["3"] = True
        return self.a_s_r_over_history

    # get four = [s_t, a_t, r, s_t+1, episode_over]
    def update_four(self, a_s_r_over_history):
        for i in range(len(a_s_r_over_history)):
            four = [{}, 0, 0, {}, False]
            if i != len(a_s_r_over_history)-1:
                four[0] = a_s_r_over_history[i]["1"]
                four[1] = a_s_r_over_history[i]["0"]
                four[3] = a_s_r_over_history[i+1]["1"]
                four[2] = a_s_r_over_history[i]["2"]
                four[4] = a_s_r_over_history[i]["3"]
                self.four[self.index] = four
                self.index += 1
            else:
                pass

    def get_four(self):
        for i in self.data.keys():
            episode = self.data[i]
            if len(episode) <= 2:
                continue
            a_s_r = self.get_a_s_r_over(episode)
            self.update_four(a_s_r)
        return self.four

    def reward_function(self, episode_status):
        if episode_status == 0:  # dialog failed
            reward = -self.num_turns
        elif episode_status == 1:  # dialog succeed
            reward = 2*self.num_turns
        else:
            reward = -1
        return reward

    def get_status(self, state):
        for i in state["current_slots"]["inform_slots"]:
            if i == "phone_number":
                episode_status = 1  # dialog succeed
                break
            else:
                episode_status = 0  # dialog failed
        return episode_status

    # input: action   output: index of action and feasible_action
    def action_index(self, action):
        del action['speaker']
        if len(action['inform_slots']) > 0:
            for slot in action['inform_slots'].keys():
                action['inform_slots'][slot] = 'PLACEHOLDER'
        equal = False
        for i in range(self.feasible_action_index):
            if operator.eq(self.feasible_action[i], action) == True:
                equal = True
                # return i
        if equal == False:
            self.feasible_action[self.feasible_action_index] = action
            self.feasible_action_index += 1
            # return self.feasible_action_index-1


if __name__ == '__main__':
    # with open('simulated_dialog.json') as f:
    #     data = json.load(f)
    # for i in data:
    #     action_set = data[i]
    #     for j in range(len(action_set)):
    #         action = action_set[j]
    #         if action['diaact'] == 'select':
    #             print(action)
    #         else:
    #             continue

    getstate = GetFour('simulated_dialog_for_test.json')
    four = getstate.get_four()
    # print(len(four.keys()))
    f = open('result_for_test.json', 'w', encoding='utf-8')
    json.dump(four, f, ensure_ascii=False)
    '''
    feasible_action = getstate.feasible_action
    f.close()
    f = open('feasible_action.json', 'w', encoding='utf-8')
    json.dump(feasible_action, f, ensure_ascii=False)
    f.close()
    '''

