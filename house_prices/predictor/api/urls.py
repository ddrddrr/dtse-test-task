from django.urls import path

from predictor.api.views import PredictHousePrice

urlpatterns = [
    path("house-price/", PredictHousePrice.as_view(), name="predict-house-price"),
]
