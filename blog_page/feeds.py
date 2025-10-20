# blog/feeds.py
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestPostsFeed(Feed):
    title = "My Blog Posts"
    link = "/blog/"
    description = "آخرین پست‌های وبلاگ من"

    def items(self):

        return Post.objects.filter(status=True).order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse("blog_page:single_post", kwargs={"pid": item.id})
