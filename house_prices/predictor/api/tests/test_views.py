from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from knox.models import AuthToken


class TestPredictHousePriceView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = "/predictions/house-price/"
        cls.valid_payload = {
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

        User = get_user_model()
        cls.user = User.objects.create_user(
            email="test@example.com", password="password123"
        )
        _, token = AuthToken.objects.create(cls.user)
        cls.token = token
        cls.client = APIClient()

    def test_authentication_required(self):
        response = self.client.post(self.url, data=self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_successful_prediction(self):
        response = self.client.post(
            self.url,
            data=self.valid_payload,
            format="json",
            headers={"Authorization": f"Token {self.token}"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("price", response.data)
        self.assertIsInstance(response.data["price"], float)

    def test_invalid_payload_returns_400(self):
        bad_payload = self.valid_payload.copy()
        bad_payload.pop("latitude")
        response = self.client.post(
            self.url,
            data=bad_payload,
            format="json",
            headers={"Authorization": f"Token {self.token}"},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("latitude", response.data)
