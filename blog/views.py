from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=True)
    template_name = "blog/index.html"
    paginate_by = 6  # control how many posts will appears per page
    # When we set the paginate_by property in the ListView class, Django adds two items to the data that is passed through to the template: a boolean value, is_paginated and a dictionary object called page_obj, which we just call the Page object.
