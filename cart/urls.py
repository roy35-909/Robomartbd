from django.urls import path
from .views import *
urlpatterns = [
    
 path('get_cart',GetCartProducts.as_view()),
 path('control_quantity',ControlQuantity.as_view()),
    
]
