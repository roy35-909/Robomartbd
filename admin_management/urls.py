from django.urls import path
from .views import *
urlpatterns = [
    
path('get_active_order',ActiveOrderManagement.as_view()),
path('get_pending_order',PendingOrderManagement.as_view()),
path('get_pending_order/<int:pk>',PendingOrderManagement.as_view()),

path('get_order/<int:pk>',OrderDetails.as_view()),


path('get_served_order',ServedOrderManagement.as_view()),
path('get_served_order/<int:pk>',ServedOrderManagement.as_view()),
path('get_dashbord',DashbordData.as_view()),
path('get_dashbord_yearly',DashbordDataYearly.as_view()),
#  path('cheak_copun',CheakCupon.as_view()),
    
]
