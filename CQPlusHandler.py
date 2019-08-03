# -*- coding:utf-8 -*-

import cqplus
import datetime
import os
now_time = datetime.datetime.now()
today_time = datetime.datetime.strftime(now_time, '%Y-%m-%d') + ".txt"
read_me_1 = "'$check'指令:根据关键词搜索今天相关的内容"
read_me_2 = "'$show'指令：列出现在所有的关键词内容"
read_me_3 = "'$clear'指令：清除目前所有关键词"
read_me_4 = "'$add''keyword'指令：增加关键词 例如$add学习，则学习为新的关键词"
class MainHandler(cqplus.CQPlusHandler):
    def handle_event(self, event, params):
        #self.logging.debug("hello world")
        if event == "on_timer":
            for key in params:
                self.logging.debug(key + " value : "+ str(type(params[key])))
#                if type(params[key]) == dict:
#                    for key2 in params[key]:
#                        if key2 == "TIMER":
#                            continue
#                        self.logging.debug(key2 + " value2 : "+ str(params[key][key2]))
                pass
        elif event == "on_private_msg":
            self.logging.debug(event)
            self.logging.debug(str(params["from_qq"]))
            self.logging.debug(params["msg"])
            self.logging.debug(str(params["msg_id"]))
            if params["msg"] == "$readme":
                cqplus._api.send_private_msg(params["env"], params["from_qq"], read_me_1)
                cqplus._api.send_private_msg(params["env"], params["from_qq"], read_me_2)
                cqplus._api.send_private_msg(params["env"], params["from_qq"], read_me_3)
                cqplus._api.send_private_msg(params["env"], params["from_qq"], read_me_4)
            if params["msg"] == "$show":
                keyword_str = open("keyword_list.txt", encoding='utf-8')
                keyword_str_line = keyword_str.read()
                if os.path.getsize("keyword_list.txt") == 0:
                    cqplus._api.send_private_msg(params["env"], params["from_qq"], "内容是空的哦！(￣▽￣)")
                else:
                    cqplus._api.send_private_msg(params["env"], params["from_qq"], keyword_str_line)
            if params["msg"] == "$clear":
               keyword_clear = open("keyword_list.txt", "w+")
               cqplus._api.send_private_msg(params["env"], params["from_qq"], "清空了哦！(●ˇ∀ˇ●)")
            if params["msg"].startswith("$add"):
                keyword_add_read = open("keyword_list.txt", encoding='utf-8')
                keyword_add_write =open("keyword_list.txt", "a+", encoding='utf-8')
                keyword_add_str = keyword_add_read.read()
                if len(keyword_add_str) > 1:
                    keyword_add_write.write('\n')
                keyword_add_write.write(params["msg"].strip("$add+"))
                cqplus._api.send_private_msg(params["env"], params["from_qq"], "添加成功了哦！(●'◡'●)")
            if params["msg"] == "jonsnow19":
                cqplus._api.send_private_msg(params["env"],params["from_qq"],"Happy Birthday!(oﾟvﾟ)ノ")

            if str(params["msg"]) == "$check":
                cqplus._api.send_private_msg(params["env"], params["from_qq"], "稍等")
                num = 0
                for line in open(today_time):
                    for lines in open("keyword_list.txt", encoding='utf-8'):
                        if line.find(lines.encode('utf-8').decode('utf-8-sig').strip()) >= 0:
                            cqplus._api.send_private_msg(params["env"], params["from_qq"], line)
                            num += 1
                if num == 0:
                    cqplus._api.send_private_msg(params["env"], params["from_qq"], "抱歉，没有找到哦(っ °Д °;)っ")
            file_log = open(today_time, "a+")
            file_log.write("类型：private ")
            file_log.write("消息ID：" + str(params["msg_id"]) + ' ')
            file_log.write("来自：" + str(params["from_qq"]) + " ")  # params["msg"] 为消息
            file_log.write("内容：" + str(params["msg"]) + " ")
            # file_log.write('\r\t')
            time1 = datetime.datetime.now()
            time1_string = datetime.datetime.strftime(time1, '%Y-%m-%d %H:%M:%S')
            file_log.write("时间：" + time1_string + "\n")
            #            for key in params:
            #                self.logging.debug(key + " value : "+ str(type(params[key])))
            #                pass

        elif event == "on_group_msg":
            self.logging.debug(event)
            for key in params:
                self.logging.debug(key + " value : " + str(params[key]))
                pass
            #cqplus._api.send_group_msg(params["env"], params["from_group"], params["msg"])
            file_log.write("类型：group ")
            file_log.write("消息ID：" + str(params["msg_id"]) + ' ')
            file_log.write("来自群：" + str(params["from_group"]) + " ")  # params["msg"] 为消息
            file_log.write("来自人：" + str(params["from_qq"]) + " ")
            file_log.write("内容：" + str(params["msg"]) + " ")
            time1 = datetime.datetime.now()
            time1_string = datetime.datetime.strftime(time1, '%Y-%m-%d %H:%M:%S')
            file_log.write("时间：" + time1_string + '\n')
