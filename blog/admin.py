from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment
# The dot in front of models indicates that we are importing Post from a file named models
# When we create a custom model and we want it to appear in the admin site


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status','created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
