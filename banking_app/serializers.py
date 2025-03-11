from rest_framework import serializers
from authorization.serializers import UserSerializer
from .models import Bank, Account


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
        queryset=Bank.objects.all(), write_only=True
    )

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

    class Meta:
        model = Account
        fields = "__all__"


class UpdateAccountSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all()
    )

    class Meta:
        model = Account
        fields = "__all__"


class GetAccountSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    user = UserSerializer()

    class Meta:
        model = Account
        fields = "__all__"


class DeleteAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"


class AccountCRUDSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all()
    )

    class Meta:
        model = Account
        fields = "__all__"

