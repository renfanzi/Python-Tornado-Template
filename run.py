#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
from app.config import settings,listen
from app.comm.util.include_url_model import url_wrapper, include
from app.comm.util.write_error import write_error




application = tornado.web.Application(url_wrapper([
    (r"", include('app.views.web_services.urls')),
], **settings))

tornado.web.RequestHandler.write_error = write_error




if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(listen)
    tornado.ioloop.IOLoop.instance().start()
