from rest_framework import serializers
from django.db.models import QuerySet
from rest_framework.fields import empty
from .models import Comment,Blog,Pages
from Basic_Api.serializers import UserCreateSerializer,ProductSerializerList

class CommentSerializer(serializers.ModelSerializer):
    commented_by = UserCreateSerializer(many=False)
    class Meta:
        model = Comment
        fields = '__all__'

class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):
    created_by = UserCreateSerializer(many=False)
    related_Product = ProductSerializerList(many=True)
    pages = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = '__all__'

    def get_pages(self,instance):
        objj = Pages.objects.filter(blog = instance)

        ser = PagesSerializer(objj,many = True)
        return ser.data



