from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # slug is what you'll use to build a URL for each of your posts.
    slug = models.SlugField(max_length=200, unique=True)
    # We used the ForeignKey field type to link one model to another
    author = models.ForeignKey(
        # relatade_name, it gives a meaningful name to the relation from the User model to the Post
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    # auto_now_add=True means the default created time is the time of post entry
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    # The primary purpose of the __str__ method is to provide a human-readable representation of the Model instance
    def __str__(self):
        return f"Post title: {self.title}. By: {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.body} by {self.author}"
