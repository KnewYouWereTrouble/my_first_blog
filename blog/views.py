from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.

def main_view(request):
    return redirect(home_view, permanent=True)

def home_view(request):
    return render(request, "blog/home.html")

def profile_view(request):
    return render(request, "blog/profile.html")


def post_view(request):
    return render(request, "blog/profile.html")




def post_details_view(request, pk):
    post = get_object_or_404(Post, title=pk)
    return render(request, "blog/post_details.html", {"p": post})
