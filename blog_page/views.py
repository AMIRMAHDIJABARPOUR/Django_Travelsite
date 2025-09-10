from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
def blog_home(request):
    posts = Post.objects.all
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)

