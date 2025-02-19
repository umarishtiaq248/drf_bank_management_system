from django.db import models
class Bank(models.Model):
    bank_name = models.CharField(max_length=128)
    branch_name = models.CharField(max_length=128)
    is_islamic = models.BooleanField(null=True)

    def __str__(self):
        return self.bank_name
