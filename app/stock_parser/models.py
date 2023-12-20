from django.db import models


class Stocks(models.Model):
    ticker = models.CharField(primary_key=True, max_length=20)
    category = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    change_percent = models.CharField(max_length=20)

    def __str__(self):
        return self.ticker

    def save_to_database(self):
        self.save()
