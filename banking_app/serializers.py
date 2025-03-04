from rest_framework import serializers
from .models import Bank, Account
from authorization.serializers import LoginSerializer

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    user_name = LoginSerializer()
    class Meta:
        model = Account
        fields = "__all__"
