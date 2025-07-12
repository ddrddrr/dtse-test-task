from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
    inline_serializer,
)
from rest_framework import serializers
from predictor.api.serializers import PredictHousePriceSerializer

predict_price_schema = extend_schema(
    request=PredictHousePriceSerializer,
    responses={
        200: OpenApiResponse(
            response=inline_serializer(
                name="PriceResponse",
                fields={
                    "price": serializers.FloatField(default=123.456),
                },
            ),
            description="Predicted house price",
        ),
        500: OpenApiResponse(
            response=inline_serializer(
                name="ErrorResponse",
                fields={
                    "detail": serializers.CharField(),
                },
            ),
            description="Unable to calculate the price.",
        ),
    },
    examples=[
        OpenApiExample(
            "Predict request",
            value={
                "longitude": -122.64,
                "latitude": 38.01,
                "housing_median_age": 36,
                "total_rooms": 1336,
                "total_bedrooms": 258,
                "population": 678,
                "households": 249,
                "median_income": 5.5789,
                "ocean_proximity": "NEAR OCEAN",
            },
            request_only=True,
        ),
    ],
)
