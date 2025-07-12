import logging

from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from predictor.api.docs import predict_price_schema
from predictor.model.wrapper import model
from predictor.api.serializers import PredictHousePriceSerializer

logger = logging.getLogger(__name__)


class PredictHousePrice(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @predict_price_schema
    def post(self, request):
        data = request.data
        ser = PredictHousePriceSerializer(data=data)
        ser.is_valid(raise_exception=True)

        try:
            price = model.predict(ser.validated_data)
        except Exception:
            logger.exception(
                f"Could not make a prediction for data {ser.validated_data}",
            )
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"detail": "Unable to calculate the price."},
            )

        return Response(status=status.HTTP_200_OK, data={"price": price})
