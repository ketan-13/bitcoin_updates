from django.urls import path
from . import views

urlpatterns = [
    #path('',views.cryptodata),
    path('',views.index),
]
