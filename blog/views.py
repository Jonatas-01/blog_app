from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6  # control how many posts will appears per page
    # When we set the paginate_by property in the ListView class, Django adds two items to the data that is passed through to the template: a boolean value, is_paginated and a dictionary object called page_obj, which we just call the Page object.

def post_detail(request, slug_url): # slug is a url parameter
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instace of :model:`blog.Post`.
    
    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1) 
    post = get_object_or_404(queryset, slug=slug_url) # first slug is a data set in post database, and we are setting the value of the parameter passed

    return render(
        request,
        "blog/post_detail.html", # template name
        {"post": post}, # context: is the variable we will use in the template to display values
    )
