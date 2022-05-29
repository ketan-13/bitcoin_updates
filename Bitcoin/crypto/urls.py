from django.urls import path
from . import views

urlpatterns = [
    path('bitcoin-default-price-list', views.index),
    path('bitcoin-price-history', views.BitcoinViewSet.as_view({'get': 'list'})),
]
