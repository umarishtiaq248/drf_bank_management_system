from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics, filters
from . import serializers
from authorization.permissions import IsStaffOrSuperUser
from .models import Bank, Account


class BankListApiView(APIView):
    def get(self, request):
        bank_qs = Bank.objects.all()
        serializer = serializers.BankSerializer(bank_qs, many=True)
        return Response(serializer.data)


class AccountListApiView(APIView):
    def get(self, request):
        queryset = Account.objects.filter(user=request.user)
        user_name = self.request.query_params.get('name')
        if user_name:
            account_qs = queryset.filter(user_name__icontains=user_name)
            serializer = serializers.AccountSerializer(account_qs, many=True)
            return Response(serializer.data)
        else:
            serializer = serializers.AccountSerializer(queryset, many=True)
            return Response(serializer.data)


class BankListViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = serializers.BankSerializer


class AccountListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AccountSerializer
    queryset = Account.objects.all()

    def get_queryset(self):
        user_name = self.request.query_params.get('name')
        if user_name:
            return self.queryset.filter(user_name__icontains=user_name)
        else:
            return self.queryset


class BankListGenericApiview(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = serializers.BankSerializer


class AccountListGenericApiview(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'user__username']


class RequestAccount(generics.ListAPIView):
    serializer_class = serializers.AccountSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Account.objects.filter(user=user)
        return queryset


class CreateBank(generics.CreateAPIView):
    serializer_class = serializers.BankSerializer


class CreateUserAccount(generics.CreateAPIView):
    serializer_class = serializers.CreateAccountSerializer

class UpdateUserAccount(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = serializers.UpdateAccountSerializer
    permission_classes = [IsStaffOrSuperUser]
    lookup_field = 'id'

