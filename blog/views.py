from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
class GetComment(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format = None):
        obj = Comment.objects.filter(commented_by=request.user)  
        ser = CommentSerializer(obj,many = True)
        return Response(ser.data)

    def post(self,request,format = None):
        data = request.data
        blog = Blog.objects.get(id = data['blog'])
        obj = Comment(commented_by=request.user,blog=blog,comment=data['comment'])
        obj.save()
        obj_ser = CommentSerializer(obj)
        return Response(obj_ser.data)
    
    def delete(self,request,format = None):
        data = request.data
        comment = Comment.objects.get(id=data['comment'])
        if comment.commented_by== request.user:
            comment.delete()
            return Response({"Success":"Successfully Deleted"})
        else:
            return Response({"Error": "You are not creator of this Comment"})
       
    
class GetAllComment(APIView):
    permission_classes = []
    def get(self,request,pk,format = None):
        
        try:
            blog = Blog.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return Response({'error':'Blog not found by this id'})
        obj = Comment.objects.filter(blog=blog)
        ser = CommentSerializer(obj,many=True,context = {'request':request})
        return Response(ser.data,status=status.HTTP_200_OK)



class GetAllBlog(APIView):
    permission_classes = []

    def get(self,request,format = None):
        blog = Blog.objects.all()
        ser = BlogSerializer(blog,many = True, context = {'request':request})
        return Response(ser.data,status=status.HTTP_200_OK)


class GetBlog(APIView):
    permission_classes = []

    def get(self,request,pk,format = None):
        try:
            blog = Blog.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return Response({'error':'Blog not found'},status=status.HTTP_404_NOT_FOUND)
        ser = BlogSerializer(blog,context = {'request':request})
        return Response(ser.data,status=status.HTTP_200_OK)
    
class GetBlogByCategory(APIView):
    permission_classes = []

    def get(self,request,pk,format = None):
        try:
            category = BlogCategory.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return Response({'error':'Category Not Found by this id'},status=status.HTTP_404_NOT_FOUND)
        
        blog = Blog.objects.filter(category=category)
        ser = BlogSerializer(blog,context = {'request':request})
        return Response(ser.data,status=status.HTTP_200_OK)