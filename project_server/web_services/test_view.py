#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import logging


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("hello")
        # logging.WARNING("this is my fasdf")
        """定义自己的日志系列，触发条件写入日志"""
        self.logger = logging.getLogger("dudu")
        if True:
            self.logger.warning("ddddd")
        self.render('template/test.html')


