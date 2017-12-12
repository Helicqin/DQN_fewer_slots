import random
import json
# from DialogManager.DialogManager import DM


class UserSimulator:
    def __init__(self, request_count):
        self.user_inform_slots = ["child_age", "english_level", "client_location", "reserve_location", "phone_number",
                                  "client_name", "client_gender", "know_about_ruisi", "special_need", "reserve_time",
                                  "child_grade", "user_goal"]
        self.user_request_slots = ['school_location', 'attend_class_alone', 'allow_parents_together', 'class_length',
                                   'textbook', 'class_size', 'teacher_nation', 'class_type', 'online_course', 'fee']
        self.agent_request_slot = ""
        self.dict_inform = {
               "user_goal": ["加盟", "预约", "咨询"],
               "client_gender": ["爸爸", "妈妈", "奶奶", "爷爷", "舅舅", "姥姥", "姥爷"],
               "child_name": ['小小艾', '小小思', "小小邺"],
               "child_age": ["1岁", "2岁", "3岁", "4岁", "5岁", "6岁", "7岁", "8岁", "9岁"],
               "english_level": ["还行", "学过", "有接触", "没接触"],
               "special_need": ["听力", "口语", "写作", "单词"],
               "client_location": ["北京市海淀区", "北京市东城区", "北京市西城区", "北京市昌平区", "北京市朝阳区"],
               "reserve_location": ["保福寺校区", "", "", "", "", ""],
               "phone_number": ["18808770123", "18808770133", "18809770123", "18808773123", "18808774123", "18808775123"],
               "client_name": ["徐小艾", "刘思思", "何邺", "李雷", "韩梅梅"],
               "know_about_ruisi": ["听说过", "没听说过"],
               "reserve_time": ["周六", "周日"],
               "child_grade": []
        }
        # 产生count个request slots,slot相对顺序仍然与user_request_slots保持一致
        self.goal = sorted(random.sample(self.user_request_slots, request_count), key=self.user_request_slots.index)
        self.dialog = []

    def user_response(self, agent_diaact):
        if agent_diaact['diaact'] == 'request' and agent_diaact['request_slots'] != {}:
            user_current_inform_slot = {}
            for i in agent_diaact['request_slots'].keys():
                user_current_inform_slot[i] = random.choice(self.dict_inform[i])  # user 对于agent的问题做出的回答

            prob = random.random()
            if prob > 0.5:
                # 用户只回答agent问题
                user_diaact = {"diaact": "inform", "request_slots": {}, "inform_slots":
                {list(user_current_inform_slot.keys())[0]: list(user_current_inform_slot.values())[0]}}
            elif 0.1 < prob < 0.5:
                # 问and答
                if self.goal != []:
                    user_current_request_slot = random.choice(self.goal)  # user要问的问题
                    # print("用户当前选择问的问题",user_current_request_slot)
                    user_diaact = {"diaact": "request",
                                   "request_slots": {user_current_request_slot: "UNK"},
                                   "inform_slots": {list(user_current_inform_slot.keys())[0]:
                                                    list(user_current_inform_slot.values())[0]}}
                    self.goal.remove(user_current_request_slot)
                else:
                    user_diaact = {"diaact": "inform", "request_slots": {},
                                   "inform_slots": {list(user_current_inform_slot.keys())[0]: list(user_current_inform_slot.values())[0]}}
            # 用户只问问题 不回答问题
            else:
                if self.goal != []:
                    user_current_request_slot = random.choice(self.goal)  # user要问的问题
                    user_diaact = {"diaact": "inform",
                                   "request_slots": {user_current_request_slot: "UNK"},
                                   "inform_slots": {}}
                    self.goal.remove(user_current_request_slot)
                else:
                    user_diaact = {"diaact": "bye", "request_slots": {}, "inform_slots": {}}
        elif agent_diaact['diaact'] == 'confirm':  # ???
            user_diaact = {'diaact': 'confirm_answer', 'request_slots': 'UNK', 'inform_slots': agent_diaact['inform_slots']}
        elif agent_diaact['diaact'] == 'select':
            l = json.loads(agent_diaact['inform_slots']['reserve_location'])
            # print('思思', [list(school.keys())[0] for school in l])
            user_diaact = {'diaact': 'inform', "request_slots": {}, "inform_slots": {"reserve_location":
                            random.choice([list(school.keys())[0] for school in l])}}
        else:
            user_diaact = {'diaact': 'bye', 'request_slots': {}, 'inform_slots': {}}
        return user_diaact

    def store_diaact(self, diaact, speaker):
        if speaker == "user":
            diaact["speaker"] = "user"
        else:
            diaact["speaker"] = "agent"
        self.dialog.append(diaact)
'''
dialog = {}
dialog_num = 1000
for i in range(dialog_num):
    dm = DM()
    user = UserSimulator(random.randint(1, 5))
    print("goal:", user.goal)
    user_diaact = {"diaact": "inform", "request_slots": {}, "inform_slots": {"user_goal": "预约"}}
    while True:
        if user_diaact["diaact"] == "bye":
            user.store_diaact(user_diaact, 'user')
            # print("user_diaact: ", user_diaact)
            break
        user.store_diaact(user_diaact, 'user')
        # print("user_diaact: ", user_diaact)
        agent_diaact = dm.agent_response_with_diaact(user_diaact)
        # print("agent_diaact: ", agent_diaact)
        user.store_diaact(agent_diaact, 'agent')
        user_diaact = user.user_response(agent_diaact)
    print("dialog {}:".format(i), user.dialog)
    dialog[str(i)] = user.dialog

with open("simulated_dialog.json", 'w', encoding='utf-8') as f:
    json.dump(dialog, f, ensure_ascii=False)
'''










