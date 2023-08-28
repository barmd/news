from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from blog.models import Post, HitCount, SideBar

###HOME

def home(request):
    posts = Post.objects.all().order_by('-date')[3:]
    sidebar = Post.objects.all().order_by('-date')[6:8]
    top_post = Post.objects.all().order_by('-date')[:1]
    top_post_two = Post.objects.all().order_by('-date')[1:2]
    top_post_three = Post.objects.all().order_by('-date')[2:3]
    context = {
        "post_list": posts,
        'top_post_two': top_post_two,
        'top_post_three': top_post_three,
        "top_post": top_post,
        "sidebar": sidebar
    }

    return render(request, 'home.html', context)


####POSTLIST

class PostListView(ListView):
    model = Post


    def get_queryset(self):
        return Post.objects.select_related('category').filter(category__slug=self.kwargs.get("slug"))

####SIDEBAR

def sidebar_details(request, id):
    sidebar = get_object_or_404(SideBar, id=id)
    return render(request, 'blog/sideBar_detail.html', {"sidebar": sidebar})
    

####POSTDETAIL
def post_details(request, id):
    post = Post.objects.filter(id=id).first()
    if post:
            hit_count, created = HitCount.objects.get_or_create(
                post=post,
                ip=request.META.get('REMOTE_ADDR', None)
            )


    return render(request, 'blog/post_detail.html', {"post":post})





 