from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta: ##used to tell django while model should be used to create the form
        model = Post
        fields = ('title', 'text')




        
