from django.urls import path
from . import views

urlpatterns = [
    path('api/bank-list/',views.bank_view,name='bank_view')
]