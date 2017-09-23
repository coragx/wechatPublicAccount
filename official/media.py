# -*- coding: utf-8 -*-
# filename: media.py
# function: 上传临时素材，获取mediaId
from basic import Basic
import urllib2
import json
import poster.encode
from poster.streaminghttp import register_openers

class Media(object):
    def __init__(self):
        register_openers()
    #上传图片
    def upload(self, accessToken, filePath, mediaType):
        openFile = open(filePath, "rb")
        param = {'media': openFile}
        # 将图片数据和headers编码
        postData, postHeaders = poster.encode.multipart_encode(param)
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        request = urllib2.Request(postUrl, postData, postHeaders)
        # 发送post请求
        urlResp = urllib2.urlopen(request)
        # 读取自动跳转url
        hjson = json.loads(urlResp.read())
        mediaId =  hjson['media_id']
        return mediaId
        
# 作为脚本执行时，发送二维码图片
if __name__ == '__main__': 
    myMedia = Media()
    accessToken = Basic().get_access_token()
    filePath = "/home/pi/media/qrcode.png"
    mediaType = "image"
    myMedia.upload(accessToken, filePath, mediaType)