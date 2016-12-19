#!/usr/bin/env python
# -*- coding:utf-8 -*-

import config
from hashlib import sha1
import os
import time
import memcache
import json
import redis

"""
注释：这个是tornado封装的session
适用于cache , memcache, redis
注意需要使用那个需要在config.py 里面拿数据才ok

同时把之前的tornado.web继承 的类用tornado的钩子函数封装，并继承，然后调用即可
这个类在core.request_handler.py
"""

create_session_id = lambda: sha1(bytes('%s%s' % (os.urandom(16), time.time()), encoding='utf-8')).hexdigest()


class SessionFactory:
    @staticmethod
    def get_session_obj(handler):
        obj = None

        if config.SESSION_TYPE == "cache":
            obj = CacheSession(handler)
        elif config.SESSION_TYPE == "memcached":
            obj = MemcachedSession(handler)
        elif config.SESSION_TYPE == "redis":
            obj = RedisSession(handler)
        return obj


class CacheSession:
    session_container = {}
    session_id = "__sessionId__"

    def __init__(self, handler):
        self.handler = handler
        client_random_str = handler.get_cookie(CacheSession.session_id, None)
        if client_random_str and client_random_str in CacheSession.session_container:
            self.random_str = client_random_str
        else:
            self.random_str = create_session_id()
            CacheSession.session_container[self.random_str] = {}

        expires_time = time.time() + config.SESSION_EXPIRES
        handler.set_cookie(CacheSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        ret = CacheSession.session_container[self.random_str].get(key, None)
        return ret

    def __setitem__(self, key, value):
        CacheSession.session_container[self.random_str][key] = value

    def __delitem__(self, key):
        if key in CacheSession.session_container[self.random_str]:
            del CacheSession.session_container[self.random_str][key]


# class MemcachedSession:
#     def __init__(self, handler):
# 获取memcache的连接
conn = memcache.Client(['192.168.11.201:12000'], debug=True, cache_cas=True)


class MemcachedSession:
    session_id = "__sessionId__"

    def __init__(self, handler):
        self.handler = handler
        # 从客户端获取随机字符串
        client_random_str = handler.get_cookie(CacheSession.session_id, None)
        # 如果从客户端获取到了随机字符串
        #
        if client_random_str and conn.get(client_random_str):
            self.random_str = client_random_str
        else:
            self.random_str = create_session_id()
            # 设置memcache的key，和value，以及超时时间
            conn.set(self.random_str, json.dumps({}), config.SESSION_EXPIRES)
            # CacheSession.session_container[self.random_str] = {}

        # 这句存在的意义就是当改变以后会重新设置超时时间
        conn.set(self.random_str, conn.get(self.random_str), config.SESSION_EXPIRES)

        expires_time = time.time() + config.SESSION_EXPIRES
        # self...设置客户端的cookie，客户端的key,value,超时时间
        handler.set_cookie(CacheSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        # ret = CacheSession.session_container[self.random_str].get(key, None)
        # 获取key
        ret = conn.get(self.random_str)
        # 转换成字典
        ret_dict = json.loads(ret)
        # none是如果没有值设置默认值
        result = ret_dict.get(key, None)
        return result

    def __setitem__(self, key, value):
        # 获取key
        ret = conn.get(self.random_str)
        ret_dict = json.loads(ret)
        # 这是字典里面的内容
        ret_dict[key] = value
        # 设置超时时间
        conn.set(self.random_str, json.dumps(ret_dict), config.SESSION_EXPIRES)

        # CacheSession.session_container[self.random_str][key] = value

    def __delitem__(self, key):
        ret = conn.get(self.random_str)
        ret_dict = json.loads(ret)
        del ret_dict[key]
        conn.set(self.random_str, json.dumps(ret_dict), config.SESSION_EXPIRES)


pool = redis.ConnectionPool(host='192.168.72.128', port=6379)
r = redis.Redis(connection_pool=pool)


class RedisSession:
    session_id = "__sessionId__"

    def __init__(self, handler):
        self.handler = handler

        client_random_str = handler.get_cookie(CacheSession.session_id, None)

        if client_random_str and r.exists(client_random_str):
            self.random_str = client_random_str
        else:
            self.random_str = create_session_id()
            r.hset(self.random_str, None, None)

        r.expire(self.random_str, config.SESSION_EXPIRES)

        expires_time = time.time() + config.SESSION_EXPIRES
        handler.set_cookie(RedisSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        result = r.hget(self.random_str, key)
        if result:
            ret_str = str(result, encoding='utf-8')
            try:
                result = json.loads(ret_str)
            except:
                result = ret_str
            return result
        else:
            return result

    def __setitem__(self, key, value):
        if type(value) == dict:
            r.hset(self.random_str, key, json.dumps(value))
        else:
            r.hset(self.random_str, key, value)

    def __delitem__(self, key):
        r.hdel(self.random_str, key)
