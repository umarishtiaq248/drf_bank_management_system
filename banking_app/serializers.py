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
