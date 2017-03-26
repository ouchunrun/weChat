# -*- coding: utf-8 -*-

# 微信接口开发

#
import json
import os
import urllib2
import xml.etree.cElementTree as ET

from weChat.settings import BASE_DIR
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class OpenConfig(object):
    """
    配置文件
    """
    def __init__(self):
        self.path = os.path.join(BASE_DIR, "message/tempates/config.xml")
        self.xml_tree = ET.ElementTree(file=self.path)

    def getAppId(self):
        self.appID = self.xml_tree.find("appID").text
        return self.appID

    def getAppSecret(self):
        self.appSecret = self.xml_tree.find("appSecret").text
        return self.appSecret


class AccessToken(object):
    """ 获取 access_token """

    def __init__(self):
        config = OpenConfig()
        self.appID = config.getAppId()
        self.appSecret = config.getAppSecret()
        self.__accseeToken = ''

    def get_access_token(self):
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
                   "client_credential&appid=%s&secret=%s" % (self.appID, self.appSecret))
        urlResp = urllib2.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())

        self.__accseeToken = urlResp["access_token"]
        return self.__accseeToken


class Authorized(object):
    """
    用户同意授权
    """

    def __init__(self):
        config = OpenConfig()
        self.appID = config.getAppId()
        self.appSecret = config.getAppSecret()

    def getCode(self, redirect_url):
        """
        获取code, 并跳转到指定界面
        :return: 
        """
        request_url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid= " + self.appID + \
                      "&redirect_uri=" + redirect_url + \
                      "&response_type=code&state=hello#wechat_redirect"
        req = urllib2.Request(request_url)
        urllib2.urlopen(req)

    def getAcToken(self, code):
        """
        通过code换取网页授权access_token
        :return: 
        """
        request_url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=" + self.appID + \
                      "&secret=" + self.appSecret + \
                      "&code=" + code + \
                      "&grant_type=authorization_code"
        req = urllib2.Request(request_url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        jsonreturn = json.loads(the_page)
        if jsonreturn.has_key('errcode'):
            return None  # 请求出现错误
        return jsonreturn

class Menu(object):
    """
    自定义菜单栏
    """

    def __init__(self):
        pass

    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib2.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib2.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib2.urlopen(url=postUrl)
        print urlResp.read()

    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib2.urlopen(url=postUrl)
        print urlResp.read()


