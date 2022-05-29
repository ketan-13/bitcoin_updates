import requests
from .models import Item,CryptoPriceHistory

def fetch_price():

    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=INR&include_market_cap=true&include_24hr_change=true&include_last_updated_at=true'
    response = requests.get(url)
    data = response.json()

    CryptoPriceHistory.objects.create(currency='bitcoin', price_inr = data['bitcoin']['inr'])
