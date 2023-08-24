from rest_framework import serializers
from django.db.models import QuerySet
from rest_framework.fields import empty
from .models import Comment,Blog
from Basic_Api.serializers import UserCreateSerializer,ProductSerializerList

class CommentSerializer(serializers.ModelSerializer):
    commented_by = UserCreateSerializer(many=False)
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    created_by = UserCreateSerializer(many=False)
    related_Product = ProductSerializerList(many=True)
    class Meta:
        model = Blog
        fields = '__all__'


