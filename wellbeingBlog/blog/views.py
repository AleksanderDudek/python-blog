from django.shortcuts import render, get_object_or_404
from .models import BlogPost
# Create your views here.

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})

#nazwa argumentu musi się zgadzać z URLem
def detail(request, postId):
    post = get_object_or_404(BlogPost, pk=postId)
    return render(request, 'detail.html', {'post': post})
