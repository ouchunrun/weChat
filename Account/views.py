# coding=utf-8
from django.shortcuts import render


def accountSave(req):
    """
    记账
    :param req: 
    :return: 
    """
    return render(req, "accountSave.html")

def accountList(req):
    """
    我的账单
    :param req: 
    :return: 
    """
    return render(req, "accountList.html")