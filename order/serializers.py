from rest_framework import serializers
from django.db.models import QuerySet
from Basic_Api.models import User,Product
from rest_framework.fields import empty
from .models import Order,OrderItem
from Basic_Api.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        exclude = ('user',)


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ('total_price','order_date','is_served','address','phone')


 