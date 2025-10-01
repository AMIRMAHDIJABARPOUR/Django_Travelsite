# blog/feeds.py
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestPostsFeed(Feed):
    title = "My Blog Posts"  # عنوان Feed
    link = "/blog/"  # لینک پایه سایت یا اپت
    description = "آخرین پست‌های وبلاگ من"  # توضیح کوتاه Feed

    def items(self):
        # آخرین 5 پست منتشر شده
        return Post.objects.filter(status=True).order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title  # عنوان هر پست

    def item_description(self, item):
        return item.content  # محتوای هر پست

    def item_link(self, item):
        # لینک مستقیم به پست
        return reverse("blog_page:single_post", kwargs={"pid": item.id})
