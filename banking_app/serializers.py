from rest_framework import serializers
from .models import Bank, Account
from authorization.serializers import UserSerializer


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    user = UserSerializer()

    class Meta:
        model = Account
        fields = "__all__"
