from django.db import models

from django.utils import timezone


class Newupdatesnack(models.Model):
    snack_name = models.CharField(max_length = 50)
    snack_brand = models.CharField(max_length = 100)
    snack_producer = models.CharField( max_length = 100)
    snack_price = models.IntegerField(default=0)
    snack_stock_unit = models.CharField( max_length = 10)
    quantity = models.PositiveIntegerField(default =0)
