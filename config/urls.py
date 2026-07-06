##############################django import#####################################
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from debug_toolbar.toolbar import debug_toolbar_urls

##############################directly_import###################################
from .sitemaps import StaticViewSitemap
from django.conf import settings
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
        path("accounts/", include("accounts.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + debug_toolbar_urls()
)
