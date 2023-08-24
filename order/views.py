from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import *
from .serializers import *

class GetOrder(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format = None):
        obj = Order.objects.filter(user=request.user)  
        ser = OrderSerializer(obj,many = True)
        return Response(ser.data)

    def post(self,request,format = None):
        obj = Order(user=request.user)
        obj.save()
        data = request.data
        price = 0
        delevary = Delivary.objects.get(code=data['delevary'])
        price+=delevary.price
        for i in data['item']:
            product = Product.objects.get(id=i['product'])
            price+=(product.price*i['count'])
            order_item = OrderItem(order=obj,product=product,quantity=i['count'])
            order_item.save()
       
        obj.total_price = price
        obj.address = data['address']
        obj.phone = data['phone']
        obj.save()
        obj_ser = OrderSerializer(obj)
        return Response(obj_ser.data)
    
    """
    def delete(self,request,format = None):
        print("Hello world")
        data = request.data
        product = Product.objects.get(id=data['product'])
        obj = Cart.objects.get(user = request.user)
        obj.products.remove(product)
        obj.count = obj.products.all().count()
        obj.save()
        ser = CartSerializerList(obj)
        return Response(ser.data)
"""

