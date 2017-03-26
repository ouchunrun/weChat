# -*- coding: utf-8 -*-
#
# 逻辑视图
#
import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from message.public import Authorized, Menu, AccessToken

access_token = AccessToken().get_access_token()

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


def login(req):
    authorized = Authorized()
    if "code" in req.GET:
        code = req.GET["code"]
        access_token, openid = authorized.getAcToken(code)
        userInfo = authorized.getUserInfo(access_token, openid)
        return render(req, "userInfo.html", {"user": userInfo})
    else:
        request_url = authorized.getCode("http://www.wangzhiwen.top/login")
        return HttpResponseRedirect(request_url)


def make_menu(req):
    """ 自定义菜单创建 """

    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "type": "view",
                "name": "个人博客",
                "url": "http://wangzhiwen.top/login/?"
            },
            {
                "name": "快捷服务",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "成绩查询",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "天气查询",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "我的京东",
                        "url": "http://re.jd.com/"
                    }
                ]
            },
            {
                "name": "娱乐一下",
                "sub_button":  
                [
                    {
                        "type": "view",
                        "name": "这里有笑话呢",
                        "url": "http://wangzhiwen.top/getJoke"
                    },
                    {
                        "type": "view",
                        "name": "你给我留言",
                        "url": "http://wangzhiwen.top/message"
                    }
                ]
            }  
        ]
    }
    """
    myMenu.create(postJson, access_token)
    myMenu.query(access_token)
    return HttpResponse(11)

