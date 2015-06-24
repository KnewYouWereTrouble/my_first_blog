from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.

def main_view(request):
    return redirect(home_view, permanent=True)

def home_view(request):
    return render(request, "blog/home.html")

def profile_view(request):
    return render(request, "blog/profile.html")


def post_view(request):
    posts = Post.objects.order_by('-published_date')

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/posts_list.html', {"posts": posts})


def post_details_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_details.html", {"p": post})


def post_view_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.publish()
            return redirect('blog.views.post_details_view', pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_new.html", {"form":form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.publish()
            return redirect('blog.views.post_details_view', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})
