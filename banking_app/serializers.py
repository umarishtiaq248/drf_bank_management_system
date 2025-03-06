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

class CreateAccountSerialzer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)
    user = UserSerializer(read_only=True)


    class Meta:
        model = Account
        fields = "__all__"


    def get_user(self):
        user = self.context['request'].user
        bank = self.get_bank()
        if Account.objects.filter(user=user, bank=bank).exists():
            raise serializers.ValidationError(
                f"User {user.username} already has an account in the {bank.bank_name} bank"
            )
        return self.context['request'].user

    def get_bank(self):
        bank_id = self.initial_data['bank_id']
        try:
            bank = Bank.objects.get(id= bank_id)
        except Bank.DoesNotExist:
            raise serializers.ValidationError(f"Bank with id {bank_id} does not exist")
        return bank

    def create(self, validated_data):
        validated_data['bank'] = self.get_bank()
        validated_data['user'] = self.get_user()
        return Account.objects.create(**validated_data)