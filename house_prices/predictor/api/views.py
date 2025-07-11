from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from predictor.model.wrapper import model
from predictor.api.serializers import PredictHousePriceSerializer


class PredictHousePrice(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = PredictHousePriceSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            price = model.predict(serializer.validated_data)
        except Exception as ex:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(ex)}
            )

        return Response(status=status.HTTP_200_OK, data={"price": price})
