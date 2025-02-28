from tkinter.font import names

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('bank-list/viewset', views.BankListViewSet,
                basename='bank-list-viewset')
router.register('account-list/viewset', views.AccountListViewSet,
                basename='account-list-viewset')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/bank-list/apiview/', views.BankListApiView.as_view(),
         name='bank-list-apiview'),
    path('api/account-list/apiview/', views.AccountListApiView.as_view(),
         name='account-list-apiview'),
    path('api/bank-list/generic_apiview/', views.BankListGenericApiview.as_view(),
         name='bank-list-generic_apiview'),
    path('api/account-list/generic_apiview/', views.AccountListGenericApiview.as_view(),
         name='account-list-generic_apiview'),
    path('api/built_in/login/', obtain_auth_token,
         name='login')
]
