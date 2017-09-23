# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            # 接收web数据
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            # 提取signature字段，timestamp字段，nonce字段，echostr字段
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            # token按照公众平台官网\基本配置中信息填写
            token = "xxxxx" 
            # 按字典序排序得到字符串list
            list = [token, timestamp, nonce]
            list.sort()
            # 哈希算法加密得到hashcode
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            # 若hashcode==signature，说明该数据源是微信后台，返回echostr供微信后台认证token
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument