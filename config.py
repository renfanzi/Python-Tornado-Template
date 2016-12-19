#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

settings = {
    'static_path': 'static',
    'static_url_prefix': '/static/',
}

listen = 8888


# Session类型：cache/redis/memcached
SESSION_TYPE = "redis"
# Session超时时间（秒）
SESSION_EXPIRES = 20

LOGIN_URL = '/login'