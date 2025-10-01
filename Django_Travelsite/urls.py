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

from debug_toolbar.toolbar import debug_toolbar_urls

##############################django import#####################################
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from debug_toolbar.toolbar import debug_toolbar_urls

##############################directly_import###################################
from .sitemaps import StaticViewSitemap
from Django_Travelsite import settings
from blog_page.sitemaps import PostSitemap, CategorySitemap
from . import views
from blog_page.feeds import LatestPostsFeed

################################################################################
sitemaps = {
    "static": StaticViewSitemap,
    "post": PostSitemap,
    "categoty": CategorySitemap,
}


urlpatterns = (
    [
        path("rss/", LatestPostsFeed(), name="post_feed"),
        path("captcha/", include("captcha.urls")),
        path("robots.txt", include("robots.urls")),
        path("sitemap.xml", views.sitemap_restricted, name="sitemap"),
        path("admin/", admin.site.urls),
        path("", include("home_page.urls")),
        path("blog_page/", include("blog_page.urls")),
        path('accounts/', include('accounts.urls')),
        path("summernote/", include("django_summernote.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + debug_toolbar_urls()
)
