from rest_framework import serializers
from django.db.models import QuerySet
from Basic_Api.models import User
from rest_framework.fields import empty
from .models import Product,Catagory,Homepage,Homeslider,Spacialoffer
from djoser.serializers import UserCreateSerializer

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','first_name','last_name','password')



class HomesliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeslider
        fields = '__all__'
class SpacialofferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeslider
        fields = '__all__'


class HomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homepage
        fields = '__all__'
    homeslider = serializers.SerializerMethodField()
    spacialoffer = serializers.SerializerMethodField()
    catagory = serializers.SerializerMethodField()
    catagorylist = serializers.SerializerMethodField()

    def get_homeslider(self,obj):
        homeslider = Homeslider.objects.filter(isactive = True)
        homeslider_serializer = HomesliderSerializer(homeslider,many = True)

        return homeslider_serializer.data
    
    def get_spacialoffer(self,obj):
        spacialoffer = Spacialoffer.objects.filter(isactive = True)
        spacialoffer_serializer = SpacialofferSerializer(spacialoffer,many = True)
        return spacialoffer_serializer.data
    
    def get_catagory(self,obj):
        catagory = Catagory.objects.filter(show_on_home = True)
        product_serializer = CatagorySerializer(catagory,many = True)
        return product_serializer.data
    def get_catagorylist(self,obj ):
        catagorylist = Catagory.objects.all()
        catagorylist_serializer = CatagoryListSerializer(catagorylist,many = True)
        return catagorylist_serializer.data



class ProductSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('catagorys','discription','after_discount','colors','stock','total_review')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CatagoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = ["id","name"]


class CatagorySerializer(serializers.ModelSerializer):
    #product = ProductSerializerList(source="product_set",many=True,read_only=True)
    product = serializers.SerializerMethodField()
    def get_product(self, obj):
        categories = obj.product_set.all()[:5]  # Get the first 5 categories
        category_serializer = ProductSerializerList(categories, many=True)
        return category_serializer.data
    class Meta:
        model = Catagory
        fields = ["id","name","product"]



