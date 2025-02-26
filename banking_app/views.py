from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import AllowAny
from rest_framework import  viewsets
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
        if user_name:
            account_qs = Account.objects.filter(user_name__icontains=user_name)
            serializer = AccountSerializer(account_qs, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No user name provided"}, status=400)

class BankListViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['get']
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class AccountListViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['get']
    serializer_class = AccountSerializer
    def get_queryset(self):
        user_name = self.request.GET.get('name')
        if user_name:
            return Account.objects.filter(user_name__icontains=user_name)
        else:
            return Response({"message": "No user name provided"}, status=400)