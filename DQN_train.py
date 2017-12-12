# -*- coding:utf8 -*-
# Created by Helic on 2017/7/27
from agent_dqn import *

params = {
    'experience_replay_pool_size': 10000,
    'dqn_hidden_size': 60,
    'gamma': 0.9,
    'predict_mode': False,
    'max_turn': 40,
    'trained_model_path': None   # 训练模式
}

agent_dqn = AgentDQN(params=params)          # 初始化参数需要改
agent_dqn.register_experience_replay_tuple_from_file('data/result.json')  # 填充经验池
agent_dqn.train(batch_size=512, num_batch=10000)
agent_dqn.save_model('data/saved_model.p')






