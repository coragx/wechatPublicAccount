# -*- coding: utf-8 -*-
# filename: receive.py
# function: 分类解析xml数据，返回特定对象

import xml.etree.ElementTree as ET
# parse_xml()函数： 
def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)           # 获取xml数据
    msg_type = xmlData.find('MsgType').text     # 提取MsgType字段，即消息类型
    if msg_type == 'text':                      # 解析文本消息
        return TextMsg(xmlData)
    elif msg_type == 'image':                   # 解析图片消息
        return ImageMsg(xmlData)
    elif msg_type == 'event':                   # 解析事件消息
        evt_type = xmlData.find('Event').text   # 提取Event字段，即事件类型
        if evt_type == 'subscribe' :            # 解析订阅事件
            return SubEvt(xmlData)

class Msg(object):  #普通消息类
    def __init__(self, xmlData):        # 初始化对象
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text

class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text.encode("utf-8")

class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text

class Evt(object):  #事件类
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.Event = xmlData.find('Event').text

class SubEvt(Evt):
    def __init__(self, xmlData):
        Evt.__init__(self, xmlData)
