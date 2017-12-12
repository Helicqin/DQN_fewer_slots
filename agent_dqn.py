# -*- coding:utf8 -*-
'''
Created on Jun 18, 2016

An DQN Agent

- An DQN
- Keep an experience_replay pool: training_data <State_t, Action, Reward, State_t+1>
- Keep a copy DQN

Command: python .\run.py --agt 9 --usr 1 --max_turn 40 --movie_kb_path .\deep_dialog\data\movie_kb.1k.json --dqn_hidden_size 80 --experience_replay_pool_size 1000 --replacement_steps 50 --per_train_epochs 100 --episodes 200 --err_method 2


@author: xiul
'''


import random, copy, json
import pickle
import numpy as np
import os

import dialog_config

from agent import Agent
from dqn import DQN


class AgentDQN(Agent):
    def __init__(self, params=None):
        # self.movie_dict = movie_dict
        self.act_set = dialog_config.act_set                           # {'request':0, 'inform':1}
        self.slot_set = dialog_config.slot_set                         # {}
        self.act_cardinality = len(self.act_set.keys())       # 5
        self.slot_cardinality = len(self.slot_set.keys())     # 15
        
        self.feasible_actions = dialog_config.feasible_actions
        self.num_actions = len(self.feasible_actions)    # 31
        
        # self.epsilon = params['epsilon']
        # self.agent_run_mode = params['agent_run_mode']
        # self.agent_act_level = params['agent_act_level']
        self.experience_replay_pool = []  # experience replay pool <s_t, a_t, r_t, s_t+1>
        
        self.experience_replay_pool_size = params['experience_replay_pool_size']
        self.hidden_size = params['dqn_hidden_size']   # 60
        self.gamma = params['gamma']                   # 0.9
        self.predict_mode = params['predict_mode']     # False
        
        self.max_turn = params['max_turn']
        # prepare_state_representation()方法返回的numpy数组的shape为(1, state_dimension),state_dimension为DQN的输入维数
        self.state_dimension = 2 * self.act_cardinality + 5 * self.slot_cardinality + 1 + self.max_turn
        self.dqn = DQN(self.state_dimension, self.hidden_size, self.num_actions)  # input_size, hidden_size, output_size
        self.clone_dqn = copy.deepcopy(self.dqn)
        
        self.cur_bellman_err = 0
                
        # Prediction Mode: load trained DQN model
        if params['trained_model_path']:
            self.dqn.model = copy.deepcopy(self.load_trained_DQN(params['trained_model_path']))
            self.clone_dqn = copy.deepcopy(self.dqn)
            self.predict_mode = True
            
    def initialize_episode(self):
        """ Initialize a new episode. This function is called every time a new episode is run. """
        
        self.current_slot_id = 0
        self.phase = 0
        self.request_set = ['moviename', 'starttime', 'city', 'date', 'theater', 'numberofpeople']

    def state_to_action(self, state):
        """ DQN: Input state, output action """
        
        self.representation = self.prepare_state_representation(state)
        self.action = self.run_policy(self.representation)
        act_slot_response = copy.deepcopy(self.feasible_actions[self.action])
        return {'act_slot_response': act_slot_response, 'act_slot_value_response': None}

    def prepare_state_representation(self, state):
        """ Create the representation for each state """
        user_action = state['user_action']
        current_slots = state['current_slots']
        agent_last = state['agent_action']
        
        ########################################################################
        #   Create one-hot of acts to represent the current user action
        ########################################################################
        user_act_rep = np.zeros((1, self.act_cardinality))
        user_act_rep[0, self.act_set[user_action['diaact']]] = 1.0

        ########################################################################
        #     Create bag of inform slots representation to represent the current user action
        ########################################################################
        user_inform_slots_rep = np.zeros((1, self.slot_cardinality))
        for slot in user_action['inform_slots'].keys():
            user_inform_slots_rep[0, self.slot_set[slot]] = 1.0

        ########################################################################
        #   Create bag of request slots representation to represent the current user action
        ########################################################################
        user_request_slots_rep = np.zeros((1, self.slot_cardinality))
        for slot in user_action['request_slots'].keys():
            user_request_slots_rep[0, self.slot_set[slot]] = 1.0

        ########################################################################
        #   Create bag of filled_in slots based on the current_slots
        ########################################################################
        current_slots_rep = np.zeros((1, self.slot_cardinality))
        for slot in current_slots['inform_slots']:
            current_slots_rep[0, self.slot_set[slot]] = 1.0

        ########################################################################
        #   Encode last agent act
        ########################################################################
        agent_act_rep = np.zeros((1, self.act_cardinality))
        if agent_last:
            agent_act_rep[0, self.act_set[agent_last['diaact']]] = 1.0

        ########################################################################
        #   Encode last agent inform slots
        ########################################################################
        agent_inform_slots_rep = np.zeros((1, self.slot_cardinality))
        if agent_last:
            for slot in agent_last['inform_slots'].keys():
                agent_inform_slots_rep[0, self.slot_set[slot]] = 1.0

        ########################################################################
        #   Encode last agent request slots
        ########################################################################
        agent_request_slots_rep = np.zeros((1, self.slot_cardinality))
        if agent_last:
            for slot in agent_last['request_slots'].keys():
                agent_request_slots_rep[0, self.slot_set[slot]] = 1.0
        
        turn_rep = np.zeros((1, 1)) + state['turn'] / 10.

        ########################################################################
        #  One-hot representation of the turn count?
        ########################################################################
        turn_onehot_rep = np.zeros((1, self.max_turn))
        turn_onehot_rep[0, state['turn']] = 1.0

        ########################################################################
        #   Representation of KB results (scaled counts)
        ########################################################################
        # kb_count_rep = np.zeros((1, self.slot_cardinality + 1)) + kb_results_dict['matching_all_constraints'] / 100.
        # for slot in kb_results_dict:
        #     if slot in self.slot_set:
        #         kb_count_rep[0, self.slot_set[slot]] = kb_results_dict[slot] / 100.

        ########################################################################
        #   Representation of KB results (binary)
        ########################################################################
        # kb_binary_rep = np.zeros((1, self.slot_cardinality + 1)) + np.sum( kb_results_dict['matching_all_constraints'] > 0.)
        # for slot in kb_results_dict:
        #     if slot in self.slot_set:
        #         kb_binary_rep[0, self.slot_set[slot]] = np.sum( kb_results_dict[slot] > 0.)
        # 水平(按列顺序)把数组给堆叠起来,函数原型：hstack(tup) ，参数tup可以是元组，列表，或者numpy数组，返回结果为numpy的数组
        self.final_representation = np.hstack([user_act_rep, user_inform_slots_rep, user_request_slots_rep,
                                               agent_act_rep, agent_inform_slots_rep, agent_request_slots_rep,
                                               current_slots_rep, turn_rep, turn_onehot_rep])
        return self.final_representation
      
    def run_policy(self, representation):
        """ epsilon-greedy policy """
        
        if random.random() < self.epsilon:
            return random.randint(0, self.num_actions - 1)
        else:
            if self.warm_start == 1:
                if len(self.experience_replay_pool) > self.experience_replay_pool_size:
                    self.warm_start = 2
                return self.rule_policy()
            else:
                return self.dqn.predict(representation, {}, predict_model=True)
    
    def rule_policy(self):
        """ Rule Policy """
        
        if self.current_slot_id < len(self.request_set):
            slot = self.request_set[self.current_slot_id]
            self.current_slot_id += 1

            act_slot_response = {}
            act_slot_response['diaact'] = "request"
            act_slot_response['inform_slots'] = {}
            act_slot_response['request_slots'] = {slot: "UNK"}
        elif self.phase == 0:
            act_slot_response = {'diaact': "inform", 'inform_slots': {'taskcomplete': "PLACEHOLDER"}, 'request_slots': {} }
            self.phase += 1
        elif self.phase == 1:
            act_slot_response = {'diaact': "thanks", 'inform_slots': {}, 'request_slots': {} }
                
        return self.action_index(act_slot_response)
    
    def action_index(self, act_slot_response):
        """ Return the index of action """
        for i in act_slot_response['inform_slots']:
            act_slot_response['inform_slots'][i] = 'PLACEHOLDER'
        # del act_slot_response['speaker']
        # if act_slot_response not in self.feasible_actions:
        #     self.feasible_actions.append(act_slot_response)
        #     print('补充action:', act_slot_response)
        for (i, action) in enumerate(self.feasible_actions):
            if act_slot_response == action:
                return i

    def index_to_action(self, action_index):
        """return the action of given index"""
        try:
            return self.feasible_actions[action_index]
        except IndexError:
            return {'diaact': "", 'inform_slots': {}, 'request_slots': {}}

    def register_experience_replay_tuple(self, s_t, a_t, reward, s_tplus1, episode_over):
        """ Register feedback from the environment, to be stored as future training data """
        
        state_t_rep = self.prepare_state_representation(s_t)
        action_t = self.action  # int
        reward_t = reward
        state_tplus1_rep = self.prepare_state_representation(s_tplus1)
        training_example = (state_t_rep, action_t, reward_t, state_tplus1_rep, episode_over)
        
        if self.predict_mode == False:  # Training Mode
            if self.warm_start == 1:
                self.experience_replay_pool.append(training_example)
                # print('pool:' + str([s_t, a_t, reward, s_tplus1]))
        else:  # Prediction Mode
            self.experience_replay_pool.append(training_example)

    def register_experience_replay_tuple_from_file(self, filename):
        """从json文件中读取(state_t_rep, action_t, reward_t, state_tplus1_rep, episode_over)"""
        f = open(filename, encoding='utf-8')
        value = json.load(f)
        f.close()
        for i in value:
            state_t_rep = self.prepare_state_representation(value[i][0])
            action_t = self.action_index(value[i][1])   # 序号
            # action_t = random.randint(0, self.num_actions-1)   # 暂时使用随机数
            reward_t = value[i][2]
            state_tplus1_rep = self.prepare_state_representation(value[i][3])
            episode_over = value[i][4]  # bool
            self.experience_replay_pool.append((state_t_rep, action_t, reward_t, state_tplus1_rep, episode_over))
        return self.experience_replay_pool

    def train(self, batch_size=1, num_batch=100):
        """ Train DQN with experience replay """
        for episode in range(num_batch):
            self.cur_bellman_err = 0
            for iter in range(int(len(self.experience_replay_pool)/batch_size)):
                batch = random.sample(self.experience_replay_pool, batch_size)
                # 从经验池中随机抽取batch_size大小的四元组，构成batch
                batch_struct = self.dqn.singleBatch(batch, {'gamma': self.gamma}, self.clone_dqn)
                self.cur_bellman_err += batch_struct['cost']['total_cost']

            print("turn %d: cur bellman err %.4f, experience replay pool %s" % (episode, float(self.cur_bellman_err)/len(self.experience_replay_pool), len(self.experience_replay_pool)))

    ################################################################################
    #    Debug Functions
    ################################################################################
    # def save_experience_replay_to_file(self, path):
    #     """ Save the experience replay pool to a file """
    #
    #     try:
    #         pickle.dump(self.experience_replay_pool, open(path, "wb"))
    #         print('saved model in %s' % (path, ))
    #     except Exception, e:
    #         print('Error: Writing model fails: %s' % (path, ))
    #         print(e)
    
    def load_experience_replay_from_file(self, path):
        """ Load the experience replay pool from a file"""
        
        self.experience_replay_pool = pickle.load(open(path, 'rb'))

    def load_trained_DQN(self, path):
        """ Load the trained DQN from a file """
        
        trained_file = pickle.load(open(path, 'rb'))
        model = trained_file['model']
        # print('trained DQN Parameters:', model)
        # print("trained DQN Parameters:", json.dumps(trained_file['params'], indent=2))
        return model

    """ Save model """
    # def save_model(self, path, agt, success_rate, agent, best_epoch, cur_epoch, params):
    #     filename = 'agt_%s_%s_%s_%.5f.p' % (agt, best_epoch, cur_epoch, success_rate)
    #     filepath = os.path.join(path, filename)
    #     checkpoint = {}
    #     if agt == 9:
    #         checkpoint['model'] = copy.deepcopy(agent.dqn.model)
    #     checkpoint['params'] = params  # 输入参数
    #     try:
    #         pickle.dump(checkpoint, open(filepath, "wb"))
    #         print 'saved model in %s' % (filepath,)
    #     except Exception, e:
    #         print 'Error: Writing model fails: %s' % (filepath,)
    #         print e
    def save_model(self, filename):
        checkpoint = {}
        checkpoint['model'] = copy.deepcopy(self.dqn.model)
        pickle.dump(checkpoint, open(filename, 'wb'))
