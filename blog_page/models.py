from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, EmailField, TextField
from taggit.managers import TaggableManager
from django.urls import reverse
from django_summernote.fields import SummernoteTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length= 128 , unique= True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('blog_page:post_filtered-by-category',kwargs={'category':self.name})
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='blog_page_home', null=True,blank=True,default='blog_page_home/default.png')
    title = models.CharField(max_length=128)
    content =SummernoteTextField()
    category = models.ManyToManyField(Category)
    tags = TaggableManager(blank=True)
    status = models.BooleanField(default = False)
    counted_views = models.IntegerField(default = 0)
    created_date = models.DateTimeField(auto_now_add = True)
    published_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog_page:single_post',kwargs={'pid':self.id})


