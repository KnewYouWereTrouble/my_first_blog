from django.shortcuts import render, redirect, get_object_or_404, render_to_response
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
    posts = Post.objects.all()
    posts_snippets = list(map(lambda x: x.text[:250], posts_list))
    posts_snippets = list(map(lambda x: x + " ...", posts_snippets))
    '''
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    '''
    return render_to_response('blog/posts_list.html', {"posts": posts})




def post_details_view(request, pk):
    post = get_object_or_404(Post, title=pk)
    return render(request, "blog/post_details.html", {"p": post})
