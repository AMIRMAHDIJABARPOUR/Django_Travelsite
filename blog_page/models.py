from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, EmailField, TextField


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length= 128 , unique= True)
    def __str__(self):
        return self.name
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='blog_page_home', null=True,blank=True,default='blog_page_home/default.png')
    title = models.CharField(max_length=128)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    # tag
    status = models.BooleanField(default = False)
    counted_views = models.IntegerField(default = 0)
    created_date = models.DateTimeField(auto_now_add = True)
    published_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title


