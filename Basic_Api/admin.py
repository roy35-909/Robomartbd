from django.contrib import admin
from .models import *
#from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Catagory)
admin.site.register(Homepage)
admin.site.register(Homeslider)
admin.site.register(Spacialoffer)
admin.site.register(User)
admin.site.register(SubCatagory)
admin.site.register(Cupon)
admin.site.register(Supplier)
admin.site.register(OurClient)