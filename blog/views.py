from django.shortcuts import render
from .models import Post

# Create your views here.

def blog(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)

def post_category(request, category):
    posts = Post.objects.filter(
        categories_name_contains = category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, slug):
    post = Post.objects.get(slug = slug)
    context = {
        "post": post,
    }
    return render(request, "blog/blog_detail.html", context)