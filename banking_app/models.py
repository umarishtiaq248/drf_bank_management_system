from django.db import models
from authorization.models import CustomUser

class Bank(models.Model):
    bank_name = models.CharField(max_length=128)
    branch_name = models.CharField(max_length=128)
    is_islamic = models.BooleanField(null=True)

    def __str__(self):
        return self.bank_name


class Account(models.Model):
    first_name= models.CharField(max_length=10,null=True)
    last_name = models.CharField(max_length=10,null=True)
    account_balance = models.FloatField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="banks")
    user_name = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user',null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
