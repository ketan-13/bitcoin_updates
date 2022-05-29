from django.db import models


class CryptoPriceHistory(models.Model):
    currency = models.CharField(max_length=100)
    price_inr = models.FloatField(max_length=10)
    price_updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.currency
