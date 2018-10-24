from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class ExpenseModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    checking = models.IntegerField(default=0)
    emergency = models.IntegerField(default=0)
    timeCreated = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.username


class Transaction(models.Model):
    depositOrWithdrawl = models.FloatField()
    account_fk = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timeOfTransaction = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.account_fk