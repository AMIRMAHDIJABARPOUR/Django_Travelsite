from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return [
            "home_page:home_main_page",
            "home_page:about_page",
            "home_page:elements",
            "home_page:contact",
            "blog_page:blog_home",
        ]

    def location(self, item):
        return reverse(item)
