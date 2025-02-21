from django import forms
from .models import Comment


class CommentForm(forms.ModelForm): # form.ModelForm is a bult-in django class
    # we use meta class to tell ModelForm what field we want in out form
    class Meta:
        model = Comment
        fields = ('body',) # included this field to user complete