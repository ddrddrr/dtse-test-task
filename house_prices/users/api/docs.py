from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
    inline_serializer,
)
from rest_framework import serializers

from users.api.serializers import LoginSerializer, RegistrationSerializer


registration_schema = extend_schema(
    request=RegistrationSerializer,
    responses={201: OpenApiResponse(description="User created")},
    examples=[
        OpenApiExample(
            "Register",
            value={"email": "new@example.com", "password": "secure!pwd"},
            request_only=True,
        ),
    ],
    tags=["authentication"],
)


# Login endpoint documentation


login_schema = extend_schema(
    request=LoginSerializer,
    responses={
        200: OpenApiResponse(
            response=inline_serializer(
                name="AuthTokenResponse",
                fields={
                    "token": serializers.CharField(),
                    "expiry": serializers.DateTimeField(),
                },
            ),
            description="Returns Knox auth token and its expiry",
        ),
        400: OpenApiResponse(description="Invalid credentials"),
    },
    examples=[
        OpenApiExample(
            "Login request",
            value={"email": "user@example.com", "password": "secret123"},
            request_only=True,
        ),
        OpenApiExample(
            "Login response",
            value={
                "token": "abcd…",
                "expiry": "2025-07-13T12:34:56Z",
            },
            response_only=True,
        ),
    ],
    tags=["authentication"],
)
