from django.shortcuts import render
from .models import Catagory,Product,Homepage,SubCatagory,OurClient,Supplier,User
from .serializers import ProductSerializer,CatagorySerializer,ProductSerializerList,HomepageSerializer,ProductSearchSerializer,OurCorporateClientSerializer,SupplierSerializer,ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist


class CatagoryList(ListAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

class HomepageView(APIView):
    def get(self,request,format = None):
        try:
            homepage = Homepage.objects.get(key = 1010)
        except:
            return Response({'error':'Give us valid homepage key'},status=status.HTTP_400_BAD_REQUEST)
        ser = HomepageSerializer(homepage,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)
    
class GetCatagoryProducts(APIView):
    def get(self,request,pk,flag,format = None):
        if flag == "category":
            try:
                products = Catagory.objects.get(id = pk)
            except:
                return Response({"error":"You Give a Unvalid Category Id"},status=status.HTTP_404_NOT_FOUND)
            sub_categorys = SubCatagory.objects.filter(category = products)
            query = products.product_set.all()
            sub_categorys_ser_data = []
            if sub_categorys.exists():
                
                for category in sub_categorys:
                    sub_products = category.product_set.all()
                    ser_sub_data = ProductSerializerList(sub_products,many=True)
                    sub_categorys_ser_data+=ser_sub_data.data

            ser = ProductSerializerList(query,many = True)
            data = ser.data + sub_categorys_ser_data

            return Response(data,status=status.HTTP_200_OK)
    
        elif flag == "subcategory":
            try:
                products = SubCatagory.objects.get(id=pk)
            except:
                return Response({"error":"Please Give an valid Subcategory id"},status=status.HTTP_404_NOT_FOUND)
            query = products.product_set.all()
            ser = ProductSerializerList(query,many = True)
            return Response(ser.data,status=status.HTTP_200_OK)
        else:
            return Response({"error":"You Miss valid Flag :)"},status=status.HTTP_406_NOT_ACCEPTABLE)

class GetProduct(APIView):
    def get(self,request,pk,format = None):
        try:
            product = Product.objects.get(id = pk)
        except:
            return Response({'error':'Product Not Found'},status=status.HTTP_404_NOT_FOUND)
        ser = ProductSerializer(product,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)


class ProductSrc(APIView):
    def get(self,request):
        #allowed = ['http://localhost:3000']
        #origin = request.META.get('HTTP_ORIGIN') # Use it On Production
        #if origin!= None and origin==allowed[0]:
        #print(origin)
        objj = Product.objects.all()
        ser = ProductSearchSerializer(objj,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
        # else:
        #     return Response({'error':'are you trying to stol our data :)'},status=status.HTTP_401_UNAUTHORIZED)

class CorporateClient(APIView):
    def get(self,request):
        objj = OurClient.objects.all()
        ser = OurCorporateClientSerializer(objj,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)


class OurSupplier(APIView):
    def get(self,request):
        objj = Supplier.objects.all()
        ser = SupplierSerializer(objj,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)

class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            
            objj = User.objects.get(email=request.user.email)
            
        except (ObjectDoesNotExist):
            return Response({'error':'User Does Not Exist'},status=status.HTTP_404_NOT_FOUND)
        ser = ProfileSerializer(objj,many = False)
        return Response(ser.data,status=status.HTTP_200_OK)
    
    def post(self,request):

        data = request.data
        user = User.objects.get(email=request.user.email)
        message = ""
        if 'phone' in data:
            user.phone = data['phone']
            message+=" Updated Phone"

        if 'address' in data:
            user.address = data['address']
            message+=" Updated address"

        if 'first_name' in data:
            user.first_name = data['first_name']
            message+=" Updated first_name"

        if 'last_name' in data:
            user.last_name = data['last_name']
            message+=" Updated last_name"

        
        if message=="":
            return Response({"error":"Provide some Data"},status=status.HTTP_406_NOT_ACCEPTABLE)
        user.save()
        return Response({"success":message},status=status.HTTP_201_CREATED)



        


