from django.template.context_processors import request
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

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

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Account
        fields = "__all__"


class UpdateRequestingUserAccountSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all()
    )

    class Meta:
        model = Account
        fields = "__all__"