# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
# 建立url映射：'/wx'到Handle函数
urls = (
    '/wx', 'Handle',
)
# 作为脚本运行时，运行web应用
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()