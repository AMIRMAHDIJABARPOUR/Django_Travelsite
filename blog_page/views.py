from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Post, Category




def blog_home(request,category=None,author=None):
    all_posts = Post.objects.all().order_by('-updated_date')
    posts = Post.objects.all().order_by('-updated_date')
    if category:
        posts=posts.filter(category__name=category)
    if author:
        posts=posts.filter(author=author)
    context = {'posts': posts,'all_posts':all_posts}
    return render(request,'blog/blog-home.html', context)
def single_post(request,pid):
    post = get_object_or_404(Post,pk=pid)
    posts = Post.objects.all().order_by('-updated_date')
    context = {'post': post , 'posts': posts}
    return render(request , 'blog/blog-single.html', context)



