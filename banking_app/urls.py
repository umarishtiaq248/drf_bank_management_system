from django.urls import path
from .views import BankListApiView,AccountListApiView

urlpatterns = [
    path('api/bank-list/',BankListApiView.as_view(),name='bank_list'),
    path('api/account-list/',AccountListApiView.as_view(),name='account_list')
]