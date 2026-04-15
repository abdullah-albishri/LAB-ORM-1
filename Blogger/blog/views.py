from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Post


def post_view(request: HttpRequest):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            Post.objects.create(title=title, content=content)
            return redirect('main:home')
    return render(request, 'blog/create.html')