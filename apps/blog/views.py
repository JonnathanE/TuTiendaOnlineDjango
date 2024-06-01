from django.shortcuts import render

from .models import Category, Post

# Create your views here.


def blogs(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(
        request, "blog/home_blog.html", {"posts": posts, "categories": categories}
    )


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, "blog/category.html", {"category": category, "posts": posts})
