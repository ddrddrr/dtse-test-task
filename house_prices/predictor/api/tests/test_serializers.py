from django.test import TestCase

from predictor.api.serializers import PredictHousePriceSerializer
from rest_framework.exceptions import ValidationError


class PredictHousePriceSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {
            "longitude": -122.64,
            "latitude": 38.01,
            "housing_median_age": 36,
            "total_rooms": 1336,
            "total_bedrooms": 258,
            "population": 678,
            "households": 249,
            "median_income": 5.5789,
            "ocean_proximity": "NEAR OCEAN",
        }

    def test_valid_data_passes(self):
        serializer = PredictHousePriceSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_missing_field_fails(self):
        data = self.valid_data.copy()
        data.pop("latitude")
        serializer = PredictHousePriceSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("latitude", serializer.errors)

    def test_boundary_values(self):
        data = self.valid_data.copy()
        data["longitude"] = 180.0
        data["latitude"] = -90.0
        serializer = PredictHousePriceSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        data["longitude"] = 180.1
        serializer = PredictHousePriceSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("longitude", serializer.errors)

    def test_invalid_proximity_fails(self):
        data = self.valid_data.copy()
        data["ocean_proximity"] = "UNKNOWN"
        serializer = PredictHousePriceSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("ocean_proximity", serializer.errors)

    def test_rooms_less_than_bedrooms_fails(self):
        data = self.valid_data.copy()
        data["total_rooms"] = 100
        data["total_bedrooms"] = 200
        serializer = PredictHousePriceSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
