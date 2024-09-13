from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        "posts" : Post,
    }
    return render(request, "index.html", context)

def help(request):
    return render(request, "help.html")

def disturbs(request):
    return render(request, "disturbs.html")

def aboutus(request):
    return render(request, "aboutus.html")