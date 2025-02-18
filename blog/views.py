from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6  # control how many posts will appears per page
    # When we set the paginate_by property in the ListView class, Django adds two items to the data that is passed through to the template: a boolean value, is_paginated and a dictionary object called page_obj, which we just call the Page object.


def post_detail(request, slug_url):  # slug is a url parameter
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instace of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    # first slug is a data set in post database, and we are setting the value of the parameter passed
    post = get_object_or_404(queryset, slug=slug_url)
    comments = post.comments.all().order_by("-created_on") # it will return all comments related to the selected post by using related_name="comments"
    comment_count = post.comments.filter(approved=True).count() # count of approved comments
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # we put it as false because we are going to populate author and post first, then we save
            comment.author = request.user #  the uyser current logged in
            comment.post = post # post is the post we took from get_object_or_404 earlier on
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm() # this line makes the form blank

    return render(
        request,
        "blog/post_detail.html",  # template name
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
         },  # all contexts: is the variable we will use in the template to display values
    )
