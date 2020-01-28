from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.

def index(request):
    all_posts=Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':all_posts})

def post_detail(request, post_id):
    post2=Post.objects.get(id=post_id)
    
    return render(request,'blog/signal.html',{'post':post2})
