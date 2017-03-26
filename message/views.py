# -*- coding: utf-8 -*-
#
# 逻辑视图
#
import hashlib

from django.http import HttpResponse
from django.shortcuts import render


def validation(req):
    """
    微信验证
    :param req: 
    :return: 
    """
    getData = req.GET
    signature = getData["signature"]
    timestamp = getData["timestamp"]
    nonce = getData["nonce"]
    echostr = getData["echostr"]
    token = "ZHYYRJYFGZS"  # 请按照公众平台官网\基本配置中信息填写

    List = [token, timestamp, nonce]
    List.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, List)
    hashcode = sha1.hexdigest()
    print "handle/GET func: hashcode, signature: ", hashcode, signature
    if hashcode == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("")
