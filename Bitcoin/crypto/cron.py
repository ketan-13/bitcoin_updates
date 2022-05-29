import requests
from .models import Item,CryptoPriceHistory

def fetch_price():

    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=INR&include_market_cap=true&include_24hr_change=true&include_last_updated_at=true'
    response = requests.get(url)
    new_data = response.json()

    for data in new_data:
        currency = data['currency']
        price_inr = data['price_inr']
        price_updated_at = data['price_updated_at']

        print(currency, price_inr, price_updated_at)

        crypto = Item.objects.get_or_create(name=name, current_price=current_price)
        CryptoPriceHistory.objects.create(crypto=crypto)
