# -*- coding: utf-8 -*-
# filename: handle.py
# funciton: 处理接收到的消息或事件推送
import hashlib
import reply
import receive
import web
import os
from basic import Basic
from media import Media

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
            
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   # 后台打印日志
            recMsg = receive.parse_xml(webData)        # 解析webData
            if isinstance(recMsg, receive.Msg):        # 若recMsg为消息类
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                print recMsg.MsgType
                if recMsg.MsgType == 'text' :
                    content = recMsg.Content
                    picPath = "/home/pi/media/%s.jpg"%content
                    #print "content is %s"%content
                    #print "picPath is %s"%picPath
                    # 若名为content的图片存在，且大小小于2M，则上传到临时素材，获得mediaId
                    if os.path.exists(picPath) and os.path.getsize(picPath) < 2097152:      
                        print "Sending picture %s.jpg, size: %sB"%(content,os.path.getsize(picPath))
                    	myMedia = Media()
                    	accessToken = Basic().get_access_token()
                    	mediaType = "image"
                    	mediaId = myMedia.upload(accessToken, picPath, mediaType)
                        # 发送图片
                        replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    	return replyMsg.send()
                    else:
                        print "%s not valid"%picPath
                    	return "success"
                else:
                    return "success"

            elif isinstance(recMsg, receive.Evt):   # 若recMsg为事件类
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                print recMsg.Event
                # 若事件类型为订阅，发送使用提示
                if recMsg.Event == 'subscribe' :    
                    #print "Sending qrcode..."
                    # 获取accessToken，上传临时素材
                    #myMedia = Media()
                    #accessToken = Basic().get_access_token()
                    #filePath = "/home/pi/media/qrcode.png"
                    #mediaType = "image"
                    #mediaId = myMedia.upload(accessToken, filePath, mediaType)
                    # 发送二维码
                    # replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    # return replyMsg.send()
                    content = "共享拍立得：请发送图片码获取图片"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                else:
                    return "success"
            else:
                print "No action"
                return "success"
        except Exception, Argument:
            return Argument


            
