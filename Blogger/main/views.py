from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from blog.models import Post


def home(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'main/home.html', {'posts': posts})
