from django.contrib import admin
from .models import Post, Comment
# The dot in front of models indicates that we are importing Post from a file named models
# When we create a custom model and we want it to appear in the admin site

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)