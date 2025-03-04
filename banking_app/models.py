from django.db import models


class Bank(models.Model):
    bank_name = models.CharField(max_length=128)
    branch_name = models.CharField(max_length=128)
    is_islamic = models.BooleanField(null=True)

    def __str__(self):
        return self.bank_name


class Account(models.Model):
    user_name = models.CharField(max_length=128)
    account_balance = models.FloatField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="accounts")

    def __str__(self):
        return f"{self.user_name}"
