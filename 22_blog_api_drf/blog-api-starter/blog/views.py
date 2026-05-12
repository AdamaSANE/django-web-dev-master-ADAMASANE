from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def show_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'post_list.html', {'posts': posts})

def show_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post.html', {'post': post})
