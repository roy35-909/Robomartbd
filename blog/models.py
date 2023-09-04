from django.db import models

from Basic_Api.models import User,Product


class Blog(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=6000,verbose_name="Write Your Description")
    related_Product = models.ManyToManyField(Product)
    image = models.ImageField(upload_to='Blog/')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.created_by.first_name} {self.created_by.last_name}"
    

class Pages(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    page_no = models.IntegerField()
    description = models.CharField(max_length=100000)
    

class Comment(models.Model):
    commented_by = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.CharField(max_length=10000)
    reply = models.CharField(max_length=10000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog.title} by {self.commented_by.first_name}"


