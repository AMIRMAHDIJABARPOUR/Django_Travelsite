from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog_page.models import Post, Category


#########################show sitemap with post.id####################
class PostSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.98

    def items(self):
        return Post.objects.all()

    def location(self, item):
        return reverse("blog_page:single_post", kwargs={"pid": item.id})

    def lastmod(self, obj):
        return obj.published_date


#########################show sitemap by category#####################
class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.99

    def items(self):
        return Category.objects.all()

    def location(self, item):
        return reverse(
            "blog_page:post_filtered-by-category", kwargs={"category": item.name}
        )
