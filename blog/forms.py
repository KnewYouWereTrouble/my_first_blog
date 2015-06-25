from django import forms
from .models import Post, Comment
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta: ##used to tell django while model should be used to create the form
        model = Post
        fields = ('title', 'snippet', 'content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "text",)
