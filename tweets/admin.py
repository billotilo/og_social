from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import UserAccount, Post, PostComment


# Minimal registration of Models.
admin.site.register(UserAccount)
admin.site.register(PostComment)


class PostCommentsInline(admin.TabularInline):
    """
    Used to show 'existing' blog comments inline below associated blogs
    """
    model = PostComment
    max_num=0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Administration object for Posts models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of post comments in blog view (inlines)
    """
    list_display = ('caption', 'useraccount', 'post_date')
    inlines = [PostCommentsInline]