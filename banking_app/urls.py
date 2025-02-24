from django.urls import path
from .views import BankListApiView

urlpatterns = [
    path('api/bank-list/',BankListApiView.as_view(),name='bank_list')
]