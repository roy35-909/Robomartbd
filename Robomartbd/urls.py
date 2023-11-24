"""
URL configuration for Robomartbd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Basic_Api.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('feedback/', include('feedback.urls')),
    path('blog/', include('blog.urls')),
    path('froala_editor/', include('froala_editor.urls')),
    path('order_management/', include('admin_management.urls')),
    # path('',include('react.urls')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
