from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import AllowAny
from .serializers import BankSerializer,AccountSerializer
from .models import Bank,Account

class BankListApiView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']
    def get(self,request):
        bank_qs = Bank.objects.all()
        serializer = BankSerializer(bank_qs,many=True)
        return Response(serializer.data)

class AccountListApiView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']
    def get(self,request):
        user_name = request.GET.get('name','')
        account_qs = Account.objects.filter(user_name__iexact=user_name)
        serializer = AccountSerializer(account_qs, many=True)
        return  Response(serializer.data)