from django.contrib import admin

from blog_page.models import Category , Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_date','status')
    list_filter = ('status','created_date','category')
    field =('author','title','status','content','category','published_date')
    date_hierarchy = 'created_date'
    search_fields = ('title','content')
    exclude = ('counted_views',)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)