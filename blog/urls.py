from django.urls import path
from .views import *
urlpatterns = [
    
 path('get_all_comment',GetAllComment.as_view()),
 path('get_comment',GetComment.as_view()),
 path('get_all_blog',GetAllBlog.as_view()),
    
]
