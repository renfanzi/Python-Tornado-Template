#!/usr/bin/env python
# -*- coding:utf-8 -*-

from project_server.web_services.test_view import MainHandler

urls = [
    (r'/aaa/', MainHandler),
]