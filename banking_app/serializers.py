from  rest_framework import serializers
from .models import Bank

class BankSerializer(serializers.Serializer):
    bank_name = serializers.CharField(max_length=128)
    branch_name = serializers.CharField(max_length=128)
    is_islamic = serializers.BooleanField(allow_null=True)
