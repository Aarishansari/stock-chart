from django.db import models

# Create your models here.
class StocksData(models.Model):
    ticker = models.CharField(max_length=10)
    description = models.TextField()
    exchange = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    class Meta:
        get_latest_by = ['ticker']
