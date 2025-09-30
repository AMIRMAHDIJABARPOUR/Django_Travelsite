from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag


def blog_home(request,category=None,author=None,tag=None):
##################################################filter posts#########################################################
    all_posts = Post.objects.all().order_by('-updated_date')
    posts = Post.objects.all().order_by('-updated_date')
    all_tags = Tag.objects.all()
    if category:
        posts=posts.filter(category__name=category)
    if author:
        posts=posts.filter(Q(author__username=author) | Q(tags__name__in=author) | Q (author__first_name=author)|Q(author__last_name=author))
    if tag:
        posts = posts.filter(tags__name__iexact=tag)
    if request.GET.get('s'):
        search_query = request.GET.get('s')
        posts = posts.filter(
            Q(title__contains=search_query) |
            Q(content__contains=search_query) |
            Q(author__username__contains=search_query) |
            Q(category__name__contains=search_query),
            status=True
        ).distinct()
################################################# end filter posts####################################################

################################################## paginator #########################################################

    paginator_posts=Paginator(posts,4)
    page_range = paginator_posts.page_range
    page_number=request.GET.get('page')
    try:
        page_obj=paginator_posts.get_page(page_number)
        # context = {'posts': posts,'all_posts':all_posts,'page_obj':page_obj,'page_range':page_range,'tags':all_tags}
    except PageNotAnInteger:
        page_obj = paginator_posts.get_page(1)
    except EmptyPage:
        page_obj = paginator_posts.get_page(paginator_posts.num_pages)
############################################### end paginator ######################################################

    context = {'posts': posts, 'all_posts': all_posts, 'page_obj': page_obj, 'page_range': page_range , 'tags': all_tags}
    return render(request,'blog/blog-home.html', context)
def single_post(request,pid):
    post = get_object_or_404(Post,pk=pid)
    posts = Post.objects.all().order_by('-updated_date')
    all_tags = Tag.objects.all()

    context = {'post': post , 'posts': posts , 'tags': all_tags}

    return render(request , 'blog/blog-single.html', context)



