"""
URL configuration for Django_Travelsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import  views
app_name = 'blog_page'
urlpatterns = [
    path('blog_home', views.blog_home, name='blog_home'),
    path('blog_home/category=<slug:category>',views.blog_home, name='post_filtered-by-category'),
    path('blog_home/author=<slug:author>',views.blog_home, name='post_filtered-by-author'),
    path('blog_home/tag=<slug:tag>',views.blog_home, name='post_filtered-by-tag'),
    path('blog_single/pid=<int:pid>', views.single_post, name='single_post'),
    path('blog_search/', views.blog_home, name='blog_search'),
]
