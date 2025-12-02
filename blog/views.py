from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    query = request.GET.get('q', '')
    
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    
    return render(request, 'blog/post_list.html', {'posts': posts, 'query': query})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
