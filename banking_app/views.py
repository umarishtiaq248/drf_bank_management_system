from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authorization.permissions import IsStaffOrSuperUser
from authorization.permissions import SelfUser
from .models import Bank, Account
from .serializers import (
    CreateAccountSerializer,
    UpdateAccountSerializer,
    BankSerializer,
    AccountSerializer,
    GetAccountSerializer,
    DeleteAccountSerializer,
    AccountCRUDSerializer
)


class BankListApiView(APIView):

    def get(self, request):
        bank_qs = Bank.objects.all()
        serializer = BankSerializer(bank_qs, many=True)
        return Response(serializer.data)


class AccountListApiView(APIView):

    def get(self, request):
        queryset = Account.objects.filter(user=request.user)
        user_name = self.request.query_params.get("name")
        if user_name:
            account_qs = queryset.filter(user_name__icontains=user_name)
            serializer = AccountSerializer(account_qs, many=True)
            return Response(serializer.data)
        else:
            serializer = AccountSerializer(queryset, many=True)
            return Response(serializer.data)


class BankListViewSet(viewsets.ModelViewSet):
    serializer_class = BankSerializer

    def get_queryset(self):
        return Bank.objects.all()


class AccountListViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer

    def get_queryset(self):
        user_name = self.request.query_params.get("name")
        if user_name:
            return Account.objects.filter(user_name__icontains=user_name)
        else:
            return Account.objects.all()


class BankListGenericApiview(generics.ListAPIView):
    serializer_class = BankSerializer

    def get_queryset(self):
        return Bank.objects.all()


class AccountListGenericApiview(generics.ListAPIView):
    serializer_class = AccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["user__first_name", "user__last_name", "user__username"]

    def get_queryset(self):
        return Account.objects.all()


class RequestAccountGenericApiview(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Account.objects.filter(user=user)
        return queryset


class CreateBankGenericApiview(generics.CreateAPIView):
    serializer_class = BankSerializer


class CreateUserAccountGenericApiview(generics.CreateAPIView):
    serializer_class = CreateAccountSerializer


class UpdateAnyUserAccountGenericApiview(generics.UpdateAPIView):
    permission_classes = [IsStaffOrSuperUser]
    serializer_class = UpdateAccountSerializer

    def get_queryset(self):
        return Account.objects.all()


class UpdateRequestingUserAccountGenericApiview(generics.UpdateAPIView):
    permission_classes = [SelfUser, IsAuthenticated]
    serializer_class = UpdateAccountSerializer

    def get_queryset(self):
        return Account.objects.all()


class GetDetailOfAnyAccountGenericApiview(generics.RetrieveAPIView):
    permission_classes = [SelfUser, IsAuthenticated]
    serializer_class = GetAccountSerializer

    def get_queryset(self):
        return Account.objects.all()


class DeleteAnyAccountGenericApiview(generics.DestroyAPIView):
    permission_classes = [SelfUser, IsAuthenticated]
    serializer_class = DeleteAccountSerializer

    def get_queryset(self):
        return Account.objects.all()


class UserAccountManagementGenericApiview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaffOrSuperUser]
    serializer_class = AccountCRUDSerializer

    def get_queryset(self):
        return Account.objects.all()