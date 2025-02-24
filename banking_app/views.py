from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import AllowAny
from .serializers import BankSerializer
from .models import Bank

class BankListApiView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']
    def get(self,request):
        bank_qs = Bank.objects.all()
        serializer = BankSerializer(bank_qs,many=True)
        return Response(serializer.data)
