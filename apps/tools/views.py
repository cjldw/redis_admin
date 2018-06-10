# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import hashlib
import redis
from utils.utils import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic.base import View


class MD5View(LoginRequiredMixin, View):
    """
    一些简单的工具处理接口
    """

    def get(self, request):
        key = request.GET.get("key")
        if key is None:
            return JsonResponse({"code": 1, "msg": "参数不能为空", "data": {"encryptkey": ""}})
        md5 = hashlib.md5()
        md5.update(key.encode("utf-8"))
        data = md5.hexdigest()
        return JsonResponse({"code": 0, "msg": "成功", "data": {"encryptkey": data}})


class RedisConnView(LoginRequiredMixin, View):
    """ceshi redis"""

    def get(self, request):
        redis_conn = redis.Redis(host="127.0.0.1", port=6379)
        return JsonResponse(redis_conn)
