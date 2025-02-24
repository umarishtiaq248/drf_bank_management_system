from django.urls import path
from .views import BankView

urlpatterns = [
    path('api/bank-list/',BankView.as_view(),name='bank_view')
]