from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length=8, required=True, write_only=True)

    class Meta:
        model = User
        fields = [
            'email', 'password', 'password_confirm', 'last_name', 'first_name'
        ]
    
    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if password_confirm != password:
            raise ValueError('Passwords didn\'t match')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    