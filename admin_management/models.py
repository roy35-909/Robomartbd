from django.db import models
from order.models import Order
class Sell(models.Model):

    order = models.ForeignKey(Order,on_delete=models.PROTECT)

    total_price = models.IntegerField()
    total_profit = models.IntegerField()

    date = models.DateField(auto_now_add=True)

    
