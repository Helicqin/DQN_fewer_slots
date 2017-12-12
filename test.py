#!/usr/bin/python
# -*- coding:utf8 -*-
# Created by Helic on 2017/7/27

import argparse
import json

# parser = argparse.ArgumentParser()
# parser.add_argument('--name', type=str, default='helic', help='username')
# parser.add_argument('--pass', type=str, default='123456', help='password')
# args = parser.parse_args()  # namespace对象
# params = vars(args)  # vars()函数以字典形式返回参数中每个成员的当前值，如果传一个对象参数则打印当前对象的属性和属性值；
# # 如果vars函数没有带参数,那么它会返回包含当前局部命名空间中所有成员的当前值的一个字典
# print(params)

# 生成slot_set{}
# set = {}
# slot_set = ['client_name', 'client_gender', 'child_name', 'child_age', 'child_grade', 'client_location',
#             'reserve_location', 'reserve_time', 'phone_number', 'english_level', 'teacher_nation', 'class_type',
#             'online_course', 'fee', 'school_location']
# for key, value in enumerate(slot_set):
#     set[value] = key
# print(set)

# f = open('new_state.json', encoding='utf-8')
# value = json.load(f)
# print(len(value.keys()))
# dic = {}
# flag = False
# for i in list(value.keys()):
#     action = value[i][0]
#     state = value[i][1]
#     j = int(i) + 1
#     if j > len(value.keys()):
#         break
#     next_state = value[str(j)][1]
#
#     if 'phone_number' in state['current_slots']['inform_slots']:
#         flag = True  # 对话成功
#         reward = 80
#     else:
#         reward = -40
#
#     if next_state['agent_action']:
#         eposide_over = False
#     else:
#         eposide_over = True
#     l = [state, action, reward, next_state, eposide_over]
#     dic[i] = l
#
# json.dump(dic, open('new_state.json', 'w', encoding='utf-8'), ensure_ascii=False)

# feasible_actions = []
# with open("data/result.json", 'r', encoding='utf-8') as f:
#     value = json.load(f)
#     for i in value:
#         agent_action = value[i][1]
#         del agent_action["speaker"]
#
#         # 修改agent_action中的inform_slots的值为PLACEHOLDER,request_slots的值为UNK
#         for j in agent_action["request_slots"]:
#             agent_action["request_slots"][j] = 'UNK'
#         for j in agent_action["inform_slots"]:
#             agent_action["inform_slots"][j] = 'PLACEHOLDER'
#
#         if agent_action not in feasible_actions:
#             feasible_actions.append(agent_action)
#             # if agent_action['diaact'] == "select" or agent_action['diaact'] == "bye":
#             #     print(agent_action)
#         else:
#             pass
# print(feasible_actions)

with open("data/result.json", 'r', encoding='utf-8') as f:
    value = json.load(f)
