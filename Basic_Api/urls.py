
from django.urls import path,include
from .views import *
urlpatterns = [
    
    path('catagorylist', CatagoryList.as_view() ),
    path('home',HomepageView.as_view()),
    path('catagory/<int:pk>', GetCatagoryProducts.as_view()),
    path('product/<int:pk>', GetProduct.as_view()),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    
]
