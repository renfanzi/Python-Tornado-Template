#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import logging.config
import logging.handlers


class log_file_cls(object):
    def log_file(self):
        # 日志初始化
        LOG_FILENAME = 'logs/logging.conf'
        logging.config.fileConfig(LOG_FILENAME)

        return logging


"""

#日志初始化
LOG_FILENAME = 'logging.conf'
logging.config.fileConfig(LOG_FILENAME)
logger = logging.getLogger("simple_log_example")

#测试代码
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

"""

# The logging program write in  __init__.py .

# and please you must log file position  ,log postion write in logs/logging.conf

"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

if you python system is python2.7,please must join ,else error

"""


# class EncodingFormatter(logging.Formatter):
#     def __init__(self, fmt, datefmt=None, encoding=None):
#         logging.Formatter.__init__(self, fmt, datefmt)
#         self.encoding = encoding
#
#
# class log_mail:
#     def log_mail(self, content):
#         errlog = logging.getLogger()
#         sh = logging.handlers.SMTPHandler("mail host (smtp host)",
#                                           '谁发的',
#                                           '发给谁',
#                                           "标题",
#                                           credentials=('用户名', '密码'),
#                                           secure=()
#                                           )
#         errlog.addHandler(sh)
#         sh.setFormatter(EncodingFormatter('%(message)s', encoding='utf-8'))
#
#         errlog.error(u'%s' % content)
