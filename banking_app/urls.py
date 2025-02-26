from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('bank-list/viewset',views.BankListViewSet,basename='bank_list-viewset')
router.register('account-list/viewset',views.AccountListViewSet,basename='account_list-viewset')

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/bank-list/apiview/',views.BankListApiView.as_view(),name='bank_list-apiview'),
    path('api/account-list/apiview/',views.AccountListApiView.as_view(),name='account_list-apiview')
]