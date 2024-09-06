from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        "posts" : Post,
    }
    return render(request, "index.html", context)