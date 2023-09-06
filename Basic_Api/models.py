from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,AbstractUser

#custom user manager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,email,first_name,last_name,password=None,**extra_fields):
        if not email:
            raise ValueError('Email is required..')
        email = self.normalize_email(email)
        user = self.model(email = email,first_name=first_name,last_name=last_name,**extra_fields)
        
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        return self.create_user(email=email,password=password,**extra_fields)

#Custom User Model
class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=500,null=True,blank=True)
    last_name = models.CharField(max_length=500,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    balance = models.IntegerField(default=0)
    balance_ref = models.CharField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=18,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    # def __str__(self) -> str:
    #     return self.email
    # def has_perm(self,perm,obj=None):
    #     return self.is_admin
    # def has_module_perms(self,app_label):
    #     return True
    # def get_full_name(self):
    #     return self.first_name+' '+self.last_name

    # @property
    # def is_staff(self):
    #     return self.staff
    # @property
    # def is_superuser(self):
    #     return self.is_admin
    objects = UserManager()


    

class Homepage(models.Model):
    key = models.IntegerField(blank=True,null=True)
    logo = models.ImageField()
    shop_poster = models.ImageField()
    phone = models.CharField(max_length=15)
    facebook = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)
    linkdin = models.CharField(max_length=200)
    twiter = models.CharField(max_length=200)
    instragram = models.CharField(max_length=200)

class Homeslider(models.Model):
    isactive = models.BooleanField(default=True)
    poster = models.ImageField()
    link = models.URLField(null=True,blank=True)

class Spacialoffer(models.Model):
    isactive = models.BooleanField(default=True)
    poster = models.ImageField()
    link = models.URLField(null=True,blank=True)


class Catagory(models.Model):
    name = models.CharField(max_length=200)
    show_on_home = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(upload_to='CategoryImage/',null=True,blank=True)
    def __str__(self) -> str:
        return self.name

class SubCatagory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='SubCategoryImage/',null=True,blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField()
    discount = models.IntegerField()
    after_discount = models.IntegerField()
    photo = models.ImageField(null=True,blank=True)
    discription = models.TextField(max_length=10000)
    ratting = models.DecimalField(max_digits=5, decimal_places=2)
    colors = models.CharField(max_length=1000)
    stock = models.IntegerField()
    total_review = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    catagorys = models.ManyToManyField(Catagory,null=True,blank=True)
    sub_catagory = models.ManyToManyField(SubCatagory,null=True,blank=True)
    buying_price = models.IntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name


class ProductMedia(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='All_Product_Additional_Photo/')

    def __str__(self) -> str:
        return self.product.name





class Review(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    r_name = models.CharField(max_length=500)
    review = models.TextField(max_length=3000)
    date = models.DateField(auto_now_add=True,null=True,blank=True)
    def __str__(self) -> str:
        return self.r_name




class Cupon(models.Model):
    cupun_code = models.CharField(max_length=200,unique=True)
    offer_name = models.CharField(max_length=500)
    price_condition = models.IntegerField()
    discount_in_percentage = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.offer_name
    




class OurClient(models.Model):
    name = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='OurClient/',null=True,blank=True)
    link = models.URLField()

    def __str__(self) -> str:
        return self.name
    

class Supplier(models.Model):
    name = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='OurSupplier/',null=True,blank=True)
    link = models.URLField()

    def __str__(self) -> str:
        return self.name
    