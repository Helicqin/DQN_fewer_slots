# 根据excel处理结果获取每句话的state

import numpy as np
import copy
class StateTracker:

    def __init__(self):
        self.initialize_episode()
        self.history_vectors = None
        self.history_dictionaries = None
        self.current_slots = None
        self.action_dimension = 10  # TODO REPLACE WITH REAL VALUE
        self.turn_count = 0

    def initialize_episode(self):           #用到的参数
        self.action_dimension = 10
        self.history_vectors = np.zeros((1, self.action_dimension))
        self.history_dictionaries = []
        self.turn_count = 0
        self.current_slots = {}

        self.current_slots['inform_slots'] = {}                #current_slots 内容还未确定
        self.current_slots['request_slots'] = {}
        self.current_slots['proposed_slots'] = {}
        self.current_slots['agent_request_slots'] = {}

    def get_state(self):
        """ Get the state representatons to send to agent """
        #state = {'user_action': self.history_dictionaries[-1], 'current_slots': self.current_slots, 'kb_results': self.kb_results_for_state()}
        #print(self.history_dictionaries)
        state = {'user_action': self.history_dictionaries[-1] if len(self.history_dictionaries) > 0 else None, 'current_slots': self.current_slots,  'turn': self.turn_count, 'history': self.history_dictionaries,
                 'agent_action': self.history_dictionaries[-2] if len(self.history_dictionaries) > 1 else None}  #删掉了kb_result
        return copy.deepcopy(state)

    #输入是非空非数字的一行，得到对应的action {'speaker':, diaact:, inform_slots:, request_slots: nl:}
    def get_action(self, list):
        name = list[0]
        nl = str(list[1])
        action = rule_nlu.get_diaact(nl)
        action['nl'] = nl
        if name == 'customer_service':
            action['speaker'] = 'agt'
        elif name == 'client':
            action['speaker'] = 'usr'
        return action

    def dialog_history_dictionaries(self):
        """  Return the dictionary representation of the dialog history (includes values) """
        return self.history_dictionaries

    def update(self, agent_action=None, user_action=None, episode_over = False):   #使用：self.state_tracker.update(agent_action=self.agent_action)  self.state_tracker.update(user_action = self.user_action)

        assert(not (user_action and agent_action)) #确认agent_action和user_action不会同时出现
        if episode_over == False:

            assert (user_action or agent_action)   #确认agent_action和user_action不会同时为空
            # 如果是agent_action，将turn speaker diaact inform_slota request_slots放入history

            if agent_action:
                # print('agent_action:', agent_action)
                agent_action_value = copy.deepcopy(agent_action)
                # agent_action_value['turn'] = self.turn_count

                for slot in agent_action_value['inform_slots']:
                    self.current_slots['proposed_slots'][slot] = agent_action_value['inform_slots'][slot]
                    self.current_slots['inform_slots'][slot] = agent_action_value['inform_slots'][
                        slot]  # add into inform_slots
                    if slot in self.current_slots['request_slots'].keys():
                        del self.current_slots['request_slots'][slot]

                for slot in agent_action_value['request_slots'].keys():
                    if slot not in self.current_slots['agent_request_slots']:
                        self.current_slots['agent_request_slots'][slot] = "UNK"

                self.history_dictionaries.append(agent_action_value)
                current_agent_vector = np.ones((1, self.action_dimension))
                self.history_vectors = np.vstack([self.history_vectors, current_agent_vector])
                # print('history:', self.history_dictionaries)

            elif user_action:
                # print('user_action:', user_action)
                for slot in user_action['inform_slots'].keys():
                    self.current_slots['inform_slots'][slot] = user_action['inform_slots'][slot]
                    if slot in self.current_slots['request_slots'].keys():
                        del self.current_slots['request_slots'][slot]

                for slot in user_action['request_slots'].keys():
                    if slot not in self.current_slots['request_slots']:
                        self.current_slots['request_slots'][slot] = "UNK"

                self.history_vectors = np.vstack([self.history_vectors, np.zeros((1, self.action_dimension))])
                user_action_value = copy.deepcopy(user_action)
                user_action_value['turn'] = self.turn_count
                self.history_dictionaries.append(user_action_value)
                # print('history:', self.history_dictionaries)

            else:
                pass
            self.turn_count += 1
        else:
            print('episode over')
            self.history_dictionaries={}
            self.turn_count = 0





'''
    def get_state(chat_data):
        state = {}
        num_episode = 0
        for i in range(len(chat_data)):
            episode_start = False
            episode_over = False
            if chat_data[i] == []:
                episode_over = True
                continue
            elif str(chat_data[i][0]).isdigit() == True:
                num_episode += 1
            else:
                action = self.get_action

'''

