from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import AllowAny
from .serializers import BankSerializer
from .models import Bank

class BankView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']
    def get(self,request):
        list_of_bank = Bank.objects.all()
        serializer = BankSerializer(list_of_bank,many=True)
        return Response(serializer.data)
