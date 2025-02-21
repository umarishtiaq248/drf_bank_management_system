from django.urls import path
from . import views

urlpatterns = [
    path('api/get/',views.bank_view,name='bank_view')
]