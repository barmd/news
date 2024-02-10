from blog.models import Category, Link,Post , HitCount
from django.shortcuts import get_object_or_404
from django.db.models import Count


def get_category_context(request):
    category = Category.objects.order_by('-date')[:5]
    context = {
        'category': category,
    }
    return context


def get_link_context(request):
    linkInst = Link.objects.all().order_by('-date')
    context = {
        'linkInst': linkInst,
    }
    return context
    

def get_post_details(request):
    most_viewed_posts = Post.objects.annotate(hit_count=Count('hitcount')).order_by('-hit_count')[:3]
    recent_post = Post.objects.all().order_by('-date')[:3]
    detailPosts = Post.objects.all().order_by('-date')[4:8]
    sidebar = Post.objects.all().order_by('-date')[6:8]
    context ={
        'most_view': most_viewed_posts,
        'recent_post' : recent_post,
        'details': detailPosts,
        "sidebar": sidebar
    }  
    return context