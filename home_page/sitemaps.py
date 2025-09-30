from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['home_page:index', 'home_page:about', 'home_page:contact', 'home_page:newsletter']

    def location(self, item):
        return reverse(item)
