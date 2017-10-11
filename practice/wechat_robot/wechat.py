# coding:utf-8
import itchat
from tuling import getResponse
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# group = []
prefix = '机器人：'


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_text_reply(msg):
    # print(msg)
    # source = msg['FromUserName']
    # print source
    response = getResponse(msg["Text"])
    if msg['isAt']:  # 在群聊中被@时才会回复
        if response.has_key('url'):
            return prefix + response["text"] + '\n' + response['url']
        else:
            return prefix + response["text"]


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # print(msg)
    response = getResponse(msg["Text"])
    if response.has_key('url'):  # 如果包含链接信息，也需要返回
        return prefix + response["text"] + '\n' + response['url']
    else:
        return prefix + response["text"]


itchat.auto_login(enableCmdQR=True)
itchat.run()
