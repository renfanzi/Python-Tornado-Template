#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import logging
from logs.log_mail import log_file_cls
# from logs.log_mail import log_mail
from comm.core.request_handler import BaseRequestHandler


class MainHandler(tornado.web.RequestHandler):
    """
    if you use session ,please you class must inherit(继承) 'BaseRequestHandler'
    and redis must content (host, post ), else: error
    so you don't have redis ,please you use 'tornado.web.ResquestHandler'
    """

    # class MainHandler(BaseRequestHandler):
    def get(self):
        # self.write("hello")
        # logging.WARNING("this is my fasdf")
        """定义自己的日志系列，触发条件写入日志"""
        # self.logger = logging.getLogger("dudu")， __name__ is file and class name
        self.logger = log_file_cls().log_file().getLogger(__name__)

        # 设置session
        # self.session["abcd"] = 123
        # print(self.session["abcd"])

        if True:
            self.logger.error("ddddd")  # 光写日志不发邮件
            # log_mail().log_mail("jjjj")     #继写日志又发邮件 注意，如果密码或网络不对会报错的,因为没有写账户密码，所以注释

        self.render('template/test.html')
