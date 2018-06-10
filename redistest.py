# -*- coding: utf-8 -*-
# website: https://loovien.github.io
# author: luowen<bigpao.luo@gmail.com>
# time: 2018/6/9 14:30
# desc:

import redis


client = None

def connect(*args, **kwargs):
    """ 连接Redis数据库，参数和redis-py的Redis类一样 """
    global client
    client = redis.Redis(*args, **kwargs)


if __name__ == "__main__":
    global client
    connect(host="127.0.0.1", port="6379")

    print client
