from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from cart.models import CartItem,Cart
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
        if "items" not in data:
            return Response({'error':'Unvalid Body Please provide product info ..'},status=status.HTTP_406_NOT_ACCEPTABLE)
        if "delevary" not in data:
            return Response({'error':'Unvalid Body Please provide delevary info ..'},status=status.HTTP_406_NOT_ACCEPTABLE)
        if "phone" not in data:
            return Response({'error':'Unvalid Body Please provide phone info ..'},status=status.HTTP_406_NOT_ACCEPTABLE)
        if "address" not in data:
            return Response({'error':'Unvalid Body Please provide phone info ..'},status=status.HTTP_406_NOT_ACCEPTABLE)

        price = 0
        try:
            delevary = Delivary.objects.get(code=data['delevary'])
        except(ObjectDoesNotExist):
            return Response({'error':'Unvalid Delevary details'},status=status.HTTP_406_NOT_ACCEPTABLE)
        price+=delevary.price
        for i in data['items']:
            try:
                product = Product.objects.get(id=i['product']['id'])
            except(ObjectDoesNotExist):
                return Response({'error':'Unvalid Product Details Please cheak ..'},status=status.HTTP_406_NOT_ACCEPTABLE)
            
            if "id" not in i:
                pass
            else:
                try:
                    cartitem = CartItem.objects.get(id=i["id"])
                except(ObjectDoesNotExist):
                    return Response({'error':'Unvalid CartItem Details Please cheak ..'},status=status.HTTP_406_NOT_ACCEPTABLE)
                try:
                    cart = Cart.objects.get(user = request.user)

                except(ObjectDoesNotExist):
                    return Response({'error':'Do You have a cart ? ..'},status=status.HTTP_406_NOT_ACCEPTABLE)
                
                if cart.price >= (cartitem.product.price*cartitem.quantity):
                    cart.price-= (cartitem.product.price*cartitem.quantity)
                    cart.save()
                
                else:
                    cart.price = 0
                    cart.save()
                cart.count-=1
                cart.save()
                cartitem.delete()
                
            
            price+=(product.price*i['quantity'])
            order_item = OrderItem(order=obj,product=product,quantity=i['quantity'])
            order_item.save()
       
        obj.total_price = price
        obj.address = data['address']
        obj.phone = data['phone']
        obj.save()
        obj_ser = OrderSerializer(obj)

        return Response(obj_ser.data,status=status.HTTP_201_CREATED)
    
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

