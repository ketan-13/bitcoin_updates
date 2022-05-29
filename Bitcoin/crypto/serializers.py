from rest_framework import serializers
from .models import CryptoPriceHistory


class CryptoPriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoPriceHistory
        fields = ['currency', 'price_inr', 'price_updated_at']
