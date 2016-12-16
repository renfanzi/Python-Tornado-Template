#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import logging
from app.logs.log_mail import log_mail


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("hello")
        # logging.WARNING("this is my fasdf")
        """定义自己的日志系列，触发条件写入日志"""
        # self.logger = logging.getLogger("dudu")
        self.logger = logging.getLogger(__name__)
        if True:
            self.logger.warning("ddddd")    #光写日志不发邮件
            log_mail().log_mail("jjjj")     #继写日志又发邮件

        self.render('template/test.html')


