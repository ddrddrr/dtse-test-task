from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

User = get_user_model()


# Reinventing auth is always a bad idea,
# but don't have the time for the test task:(
# It can be properly done e.g. with allauth/dj-rest-auth
class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already registered")
        return email

    def create(self, validated):
        return User.objects.create_user(
            email=validated["email"],
            password=validated["password"],
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs["email"],
            password=attrs["password"],
        )
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")
        attrs["user"] = user
        return attrs
