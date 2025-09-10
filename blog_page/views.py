from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Post, Category




def blog_home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)
def single_post(request,pid):
    post = get_object_or_404(Post,pk=pid)

    context = {'post': post}
    return render(request , 'blog/blog-single.html', context)
def post_filtered(request,category=None,author=None,):
    posts = Post.objects.all()
    if not category:
        posts =posts.filter(category__name=category)
    if not author:
        posts = posts.filter(author__name=author)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)