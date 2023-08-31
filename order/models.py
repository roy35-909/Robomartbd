from django.db import models
from cart.models import Cart
from Basic_Api.models import User,Product
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_served = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(blank=True,null=True)
    address = models.TextField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.user.email} => is_served: {self.is_served} => price : {self.total_price}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.order.user.email} => Product : {self.product.name}"

class Delivary(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} => Price : {self.price}"
