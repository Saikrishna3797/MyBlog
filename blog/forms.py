from django import forms
from .models import Post


class newPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','body','project')


class CommentForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )
