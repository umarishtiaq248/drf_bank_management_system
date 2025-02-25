from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import AllowAny
from rest_framework import  viewsets
from .serializers import BankSerializer,AccountSerializer
from .models import Bank,Account

class BankListApiView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['get']
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class AccountListApiView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['get']
    serializer_class = AccountSerializer
    def get_queryset(self):
        user_name = self.request.GET.get('name')
        if user_name:
            return Account.objects.filter(user_name__icontains=user_name)