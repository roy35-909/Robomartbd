from django.shortcuts import render
from .models import Catagory,Product,Homepage
from .serializers import ProductSerializer,CatagorySerializer,ProductSerializerList,HomepageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from rest_framework.permissions import IsAdminUser

class CatagoryList(ListAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

class HomepageView(APIView):
    def get(self,request,format = None):
        homepage = Homepage.objects.get(key = 1010)
        ser = HomepageSerializer(homepage,many=False)
        return Response(ser.data)
    
class GetCatagoryProducts(APIView):
    def get(self,request,pk,format = None):
        products = Catagory.objects.get(id = pk)
        query = products.product_set.all()
        ser = ProductSerializerList(query,many = True)
        return Response(ser.data)

class GetProduct(APIView):
    def get(self,request,pk,format = None):
        product = Product.objects.get(id = pk)
        ser = ProductSerializer(product,many=False)
        return Response(ser.data)
