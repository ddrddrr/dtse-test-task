from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from knox.auth import TokenAuthentication

from predictor.model_wrapper import model


class PredictHousePrice(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # validate data via serializer
        data = ...
        try:
            price = model.predict(data)
        except Exception as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_200_OK, data=price)
