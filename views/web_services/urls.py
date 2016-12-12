#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app.run import application
from app.views.web_services.test_view import MainHandler
import tornado.web


urls = [
    (r'/aaa/', MainHandler),
]