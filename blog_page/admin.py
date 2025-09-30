from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog_page.models import Category , Post
from django.urls import reverse

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ('title','author','created_date','status')
    list_filter = ('status','created_date','category')
    field = ('author','title','status','content','category','published_date')
    date_hierarchy = 'created_date'
    search_fields = ('title',)#'content'
    exclude = ('counted_views',)

    def view_on_site(self, obj=None):
        return obj.get_absolute_url()




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)
    def view_on_site(self, obj=None):
        return obj.get_absolute_url()