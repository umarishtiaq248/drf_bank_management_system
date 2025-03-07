from rest_framework import serializers
from .models import Bank, Account
from authorization.serializers import UserSerializer


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Account
        fields = "__all__"


class CreateAccountSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all(),
        write_only=True
    )

    class Meta:
        model = Account
        fields = "__all__"

    def get_user(self):
        return self.context['request'].user

    def create(self, validated_data):
        validated_data['user'] = self.get_user()
        return super().create(validated_data)


class UpdateAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"

    bank = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all(),
        write_only=True
    )

    def update(self, instance, validated_data):
        instance.account_balance = validated_data.get('account_balance', instance.account_balance)
        if 'bank' in validated_data:
            instance.bank = validated_data['bank']
        instance.save()
        return instance