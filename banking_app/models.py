from django.db import models
from authorization.models import CustomUser


class Bank(models.Model):
    bank_name = models.CharField(max_length=128)
    branch_name = models.CharField(max_length=128)
    is_islamic = models.BooleanField(null=True)

    def __str__(self):
        return self.bank_name


class Account(models.Model):
    account_balance = models.FloatField(default=0)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="banks")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='users', null=True)

    class Meta:
        unique_together = ('user', 'bank')


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
