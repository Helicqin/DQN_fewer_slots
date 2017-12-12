# Read me
** 目录 **
simulated_dialog.json: 存储由user simulator 和agent产生的对话，每个ID对应一个episode
result.json：存储从上文件的对话中提取出的五元组[s_t,a_t,r,s_t+1,episode_over]
state_tracker.py: class StateTracker 用于get_state,和追踪对话历史
get_four.py: class GetFour 得到五元组[s_t,a_t,r,s_t+1,episode_over],同时获得feasible_action，存在feasible_action.json里
feasible_action:存储agent可能的动作空间，格式：字典，每个id是一个action，action里的inform_slots的value为“PLACEHOLDER”
# How to use class GetFour?
<if __name__ == '__main__':

    getstate = GetFour('simulated_dialog.json')
    four = getstate.get_four()
    # print(len(four.keys()))
    f = open('result.json', 'w', encoding='utf-8')
    json.dump(four, f, ensure_ascii=False)
    feasible_action = getstate.feasible_action
    f.close()
    f = open('feasible_action.json', 'w', encoding='utf-8')
    json.dump(feasible_action, f, ensure_ascii=False)
    f.close()
>
# Input Format
<{
    "0": [
        {
            "diaact": "inform",
            "request_slots": {},
            "inform_slots": {
                "user_goal": "预约"
            },
            "speaker": "user"
        },
        {
            "diaact": "request",
            "request_slots": {
                "child_age": "UNK"
            },
            "inform_slots": {},
            "speaker": "agent"
        }
    ]
}>
每个ID为一个episode，每个episode里的每一项为一个diaact
# Result
<{
    "0": [
        # state
        {
            "user_action": {
                "diaact": "inform",
                "request_slots": {},
                "inform_slots": {
                    "user_goal": "预约"
                },
                "speaker": "user",
                "turn": 0
            },
            "current_slots": {
                "inform_slots": {
                    "user_goal": "预约"
                },
                "request_slots": {},
                "proposed_slots": {},
                "agent_request_slots": {}
            },
            "turn": 1,
            "history": [
                {
                    "diaact": "inform",
                    "request_slots": {},
                    "inform_slots": {
                        "user_goal": "预约"
                    },
                    "speaker": "user",
                    "turn": 0
                }
            ],
            "agent_action": {
            "diaact": "greeting",
            "request_slots": {},
            "inform_slots": {},
            "speaker": "agent"
        }
        },
        # agent_action
        {
            "diaact": "request",
            "request_slots": {
                "child_age": "UNK"
            },
            "inform_slots": {},
            "speaker": "agent"
        },
        # next state
        {
            "user_action": {
                "diaact": "inform",
                "request_slots": {},
                "inform_slots": {
                    "child_age": "1岁"
                },
                "speaker": "user",
                "turn": 2
            },
            "current_slots": {
                "inform_slots": {
                    "user_goal": "预约",
                    "child_age": "1岁"
                },
                "request_slots": {},
                "proposed_slots": {},
                "agent_request_slots": {
                    "child_age": "UNK"
                }
            },
            "turn": 3,
            "history": [
                {
                    "diaact": "inform",
                    "request_slots": {},
                    "inform_slots": {
                        "user_goal": "预约"
                    },
                    "speaker": "user",
                    "turn": 0
                },
                {
                    "diaact": "request",
                    "request_slots": {
                        "child_age": "UNK"
                    },
                    "inform_slots": {},
                    "speaker": "agent",
                    "turn": 1
                },
                {
                    "diaact": "inform",
                    "request_slots": {},
                    "inform_slots": {
                        "child_age": "1岁"
                    },
                    "speaker": "user",
                    "turn": 2
                }
            ],
            "agent_action": {
                "diaact": "request",
                "request_slots": {
                    "child_age": "UNK"
                },
                "inform_slots": {},
                "speaker": "agent",
                "turn": 1
            }
        },
        # reward
        -2
    ]
}>

每个ID对应一个五元组
每个episode的第一个五元组里的state的agent_action为greeting
** 对话状态的判断 **：每个episode结束时，最后一个state["current_slots"]["inform_slots"]里存在phone_number，即获得用户的电话号码即为成功。
** reward的制定规则 **：对话未完成则为-1，失败-num_turns,成功+2*num_turns

