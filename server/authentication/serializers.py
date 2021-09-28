from .models import User, EmailVerify
from rest_framework import serializers


class SignUp(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_verified')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user


class EmailVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerify
        fields = ['email']
