from rest_framework import serializers
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request=self.context.get('request'), username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        data['user'] = user
        return data