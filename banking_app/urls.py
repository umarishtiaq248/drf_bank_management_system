from django.urls import path,include
from .views import BankListApiView,AccountListApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('bank-list',BankListApiView,basename='bank_list')
router.register('account-list',AccountListApiView,basename='account_list')

urlpatterns = [
    path('api/',include(router.urls)),
]