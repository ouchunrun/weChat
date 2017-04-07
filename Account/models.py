from __future__ import unicode_literals

from django.db import models
from message.models import User


class Spend(models.Model):
    money = models.FloatField(db_column="money")
    useTime = models.DateTimeField(db_column="useTime")
    useThing = models.CharField(max_length=150, db_column="useThing")
    userId = models.ForeignKey(User, db_column="user")

    class Meta:
        db_table = 'Spend'


class Bill(models.Model):
    account = models.FloatField(db_column="account")
    createDate = models.DateTimeField(db_column="creatDate")
    userId = models.ForeignKey(User, db_column="user")

    class Meta:
        db_table = 'Bill'