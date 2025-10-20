from django import template
from django.db.models import Count
from operator import itemgetter
from blog_page.models import Post, Category
from collections import OrderedDict

register = template.Library()


@register.inclusion_tag("blog/show_list_of_posts_by_categories.html")
def show_list_of_posts_by_categories():
    posts = Post.objects.all()
    categories = Category.objects.all()
    category_dict = {}
    for scategory in categories:
        category_dict[scategory] = posts.filter(category=scategory).count()

    sorted_items = sorted(category_dict.items(), key=itemgetter(1), reverse=True)

    category_dict_list_of_tuples = OrderedDict(sorted_items[0:5])

    return {"category_dict_list_of_tuples": category_dict_list_of_tuples}


