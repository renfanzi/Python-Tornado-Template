#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.netutil
import tornado.process
from tornado.httpserver import HTTPServer
import tornado.httpserver
import tornado.ioloop
import tornado.web
from app.config import settings, listen
from app.comm.util.include_url_model import url_wrapper, include
from app.comm.util.write_error import write_error

application = tornado.web.Application(url_wrapper([
    (r"", include('app.project_server.web_services.urls')),
]), **settings)

tornado.web.RequestHandler.write_error = write_error

if __name__ == "__main__":
    #1.
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(listen)
    tornado.ioloop.IOLoop.instance().start()
    #3.
    # sockets = tornado.netutil.bind_sockets(8888)
    # tornado.process.fork_processes(5)
    # project_server = HTTPServer(application)
    # project_server.add_sockets(sockets)
    # tornado.ioloop.IOLoop.instance().start()

    #2.
    # server = HTTPServer(application)
    # server.bind(8888)
    # server.start(4) #Forks multiple sub-process
    # tornado.ioloop.IOLoop.current().start()