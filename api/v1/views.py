from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.tools import calculate_total_value


class TotalNumberView(APIView):
    def get(self, request):
        value = calculate_total_value()
        return Response(data={"total": value})
