# -*- coding: utf-8 -*-
# filename: basic.py
# funciton: 获取access token，若到期则自动重新获取
import urllib
import time
import json

class Basic:
    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0

    def __real_get_access_token(self):
        appId = "xxx"
        appSecret = "xxx"
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
               "client_credential&appid=%s&secret=%s" % (appId, appSecret))
        # 发送post请求
        urlResp = urllib.urlopen(postUrl)
        # 读取自动跳转url
        urlResp = json.loads(urlResp.read())
        # 获取accesstoken及其到期时间expires_in
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']

    def get_access_token(self):
        # 若accesstoken即将到期，则重新获取；否则返回已有的accesstoken
        if self.__leftTime < 10:
            self.__real_get_access_token()
        return self.__accessToken

    def run(self):
        while(True):
            # 计算到期时间
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            # 若到期，重新获取accseetoken
            else:
                self.__real_get_access_token()