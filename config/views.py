from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from .sitemaps import StaticViewSitemap
from blog_page.sitemaps import PostSitemap, CategorySitemap


@login_required
def sitemap_restricted(request):
    sitemaps = {
        "static": StaticViewSitemap,
        "post": PostSitemap,
        "categoty": CategorySitemap,
    }
    return sitemap(request, sitemaps)
