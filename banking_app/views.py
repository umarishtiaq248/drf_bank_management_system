from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics, filters
from .serializers import BankSerializer, AccountSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Bank, Account


class BankListApiView(APIView):
    def get(self, request):
        bank_qs = Bank.objects.all()
        serializer = BankSerializer(bank_qs, many=True)
        return Response(serializer.data)


class AccountListApiView(APIView):
    def get(self, request):
        queryset = Account.objects.filter(user=request.user)
        user_name = self.request.query_params.get('name')
        if user_name:
            account_qs = queryset.filter(user_name__icontains=user_name)
            serializer = AccountSerializer(account_qs, many=True)
            return Response(serializer.data)
        else:
            serializer = AccountSerializer(queryset, many=True)
            return Response(serializer.data)


class BankListViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class AccountListViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get_queryset(self):
        user_name = self.request.query_params.get('name')
        if user_name:
            return self.queryset.filter(user_name__icontains=user_name)
        else:
            return self.queryset


class BankListGenericApiview(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class AccountListGenericApiview(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name','user__last_name','user__username']

class RequestAccount(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


