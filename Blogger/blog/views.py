from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Post


def post_view(request: HttpRequest):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            poster = request.FILES.get('poster')
            post = Post(title=title, content=content)
            if poster:
                post.poster = poster
            post.save()
            return redirect('main:home')
    return render(request, 'blog/create.html')


def post_edit(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            post.title = title
            post.content = content
            poster = request.FILES.get('poster')
            if poster:
                post.poster = poster
            post.save()
            return redirect('main:home')
    return render(request, 'blog/edit.html', {'post': post})


def post_delete(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('main:home')
    return render(request, 'blog/delete.html', {'post': post})