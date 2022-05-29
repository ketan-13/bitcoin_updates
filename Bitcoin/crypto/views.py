from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
import requests

from .serializers import CryptoPriceHistorySerializer
from .models import CryptoPriceHistory


# Create your views here.
def cryptodata(request):

    name = 'bitcoin'
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=INR&include_market_cap=true&include_24hr_change=true&include_last_updated_at=true'
    response = requests.get(url)
    data = response.json()
    all_coins = [{'name': "bitcoin", "current_price": data['bitcoin']['inr']}]

    return render(request, 'coins/crypto.html', {"all_coins": all_coins})


def index(request):

    bitcoins = CryptoPriceHistory.objects.filter(currency='bitcoin').order_by('-price_updated_at')

    all_coins = bitcoins.values('currency','price_inr','price_updated_at')[:10:1]
    print(all_coins)

    return render(request, 'coins/crypto.html', {"all_coins": all_coins})


class BitcoinViewSet(viewsets.ModelViewSet):
    queryset = CryptoPriceHistory.objects.all().order_by('-price_updated_at')
    serializer_class = CryptoPriceHistorySerializer
