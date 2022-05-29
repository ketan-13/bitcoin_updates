from django.shortcuts import render
from .models import CryptoPriceHistory


def index(request):
    # todo add pagination and authorization
    bitcoins = CryptoPriceHistory.objects.filter(currency='bitcoin').order_by('-price_updated_at')
    all_coins = bitcoins.values('currency','price_inr','price_updated_at')[:10:1]
    return render(request, 'coins/crypto.html', {"all_coins": all_coins})



