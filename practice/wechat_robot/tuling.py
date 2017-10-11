# coding:utf-8
import requests
default = '你好'


def getResponse(_info=default):
    # print(_info)
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {'key': '7c1ccc2786df4e1685dda9f7a98c4ec9',  # 图灵机器人API的Key
            'info': _info,  # 需要发出去的消息
            'userid': 'wechat-robot'  # 标记你的用户ID，任意值
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    return r


# print(type(getResponse()))
# print (getResponse()['text'])
# print (getResponse()['url'])