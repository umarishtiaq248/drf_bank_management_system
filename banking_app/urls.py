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
    path('api/request-user/account/', views.RequestAccount.as_view(),
         name='request-user_account'),
    path('api/create-bank/', views.CreateBank.as_view(),
         name='create-bank'),
    path('api/create-account/', views.CreateUserAccount.as_view(),
         name='create-account'),
    path('api/update-account/<int:pk>/', views.UpdateRequestingUserAccount.as_view(),
         name='update-account'),
]
