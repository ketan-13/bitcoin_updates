from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('bitcoin-default-price-list', views.index),
    path('bitcoin-price-history', views.BitcoinViewSet.as_view({'get': 'list'})),
]
