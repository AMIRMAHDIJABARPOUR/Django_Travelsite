

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from . import views

app_name = "blog_page"
urlpatterns = [
    path("blog_home", views.blog_home, name="blog_home"),
    path(
        "blog_home/category=<slug:category>",
        views.blog_home,
        name="post_filtered-by-category",
    ),
    path(
        "blog_home/author=<slug:author>",
        views.blog_home,
        name="post_filtered-by-author",
    ),
    re_path(
        r"^blog_home/tag=(?P<tag>[-a-zA-Z0-9_]+)$",
        views.blog_home,
        name="post_filtered-by-tag",
    ),

    path("blog_single/pid=<int:pid>", views.single_post, name="single_post"),
    path("blog_search/", views.blog_home, name="blog_search"),
]
