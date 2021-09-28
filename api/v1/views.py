from rest_framework.response import Response
from rest_framework.views import APIView


class TotalNumberView(APIView):
    def get(self, request):
        return Response(data={"total": 0})
