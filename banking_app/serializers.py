from rest_framework import serializers
from .models import Bank, Account
from authorization.serializers import UserSerializer


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    bank_id = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all(),
        source='bank',
        write_only=True
    )
    bank = BankSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Account
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return Account.objects.create(**validated_data)

    def validate_bank_id(self, value):
        if not Bank.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Bank does not exist")
        return value
