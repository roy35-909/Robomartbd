from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class GetFeedback(APIView):
    permission_classes = [IsAuthenticated]
    #Get a User All Feedback
    def get(self,request,format = None):
        obj = Feedback.objects.filter(user=request.user)  
        ser = FeedbackSerializer(obj,many = True)
        return Response(ser.data)
    # Create a Feedback Of a Product
    def post(self,request,format = None):
        data = request.data
        product = Product.objects.get(id = data['product'])
        obj = Feedback(user=request.user,product=product,ratting=data['ratting'],review=data['review'])
        obj.save()
        obj_ser = FeedbackSerializer(obj)
        return Response(obj_ser.data)
    # Delete A feedback of this User and His Created Feedback
    def delete(self,request,format = None):
        data = request.data
        feedback = Feedback.objects.get(id=data['feedback'])
        if feedback.user== request.user:
            feedback.delete()
            return Response({"Success":"Successfully Deleted"})
        else:
            return Response({"Error": "You are not creator of this Feedback"})
        
#Get All FeedBack  
class GetAllFeedback(APIView):
    permission_classes = []
    def get(self,request,format = None):
        data = request.data
        product = Product.objects.get(id=data['product'])
        obj = Feedback.objects.filter(product=product)
        ser = FeedbackSerializer(obj,many = True)
        return Response(ser.data)

  

"""
    def delete(self,request,format = None):
        data = request.data
        product = Product.objects.get(id=data['product'])
        obj = Cart.objects.get(user = request.user)
        obj.products.remove(product)
        obj.count = obj.products.all().count()
        obj.save()
        ser = CartSerializerList(obj)
        return Response(ser.data)
"""


