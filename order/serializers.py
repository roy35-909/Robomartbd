from rest_framework import serializers
from django.db.models import QuerySet
from Basic_Api.models import User,Product
from rest_framework.fields import empty
from .models import Order,OrderItem
from Basic_Api.serializers import ProductSerializerList

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializerList()
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ('id','total_price','order_date','is_served','address','phone')


class OrderDetailsSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'

    def get_items(self,instance):
        objj = OrderItem.objects.filter(order = instance)
        print(objj)
        ser = OrderItemSerializer(objj,many = True,context=self._context)
        return ser.data

 