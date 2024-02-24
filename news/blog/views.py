from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic import TemplateView
from blog.forms import ContactForm
from blog.models import Post, HitCount
from django.http import HttpResponse
from .forms import PostSearchForm
from django.db import models
from django.http import JsonResponse
from django.template.loader import render_to_string


###HOME

def home(request):
    posts = Post.objects.all().order_by('-id')[3:15]
    top_post = Post.objects.all().order_by('-id')[:1]
    top_post_two = Post.objects.all().order_by('-id')[1:2]
    top_post_three = Post.objects.all().order_by('-id')[2:3]
    context = { 
        "post_list": posts,
        'top_post_two': top_post_two,
        'top_post_three': top_post_three,
        "top_post": top_post,
    }

    return render(request, 'home.html', context)


#####ContactPageviews
class ContactPageView(TemplateView):
    template_name = 'blog/contact.html'
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Bog'langaniz uchun tasahkkur!")

        context = {
            'form': form
        }

        return render(request, 'blog/contact.html', context)




###author
def author(request):
    return render(request, 'blog/author.html')

###the last post
def TheLastpost(request):
    postes = Post.objects.all().order_by('-id')[:15]
    context = {
        "last_post": postes,
    }

    return render(request, 'blog/theLastpost.html', context)


###Post list

class PostListView(ListView):
    posts = Post.objects.all().order_by('date')[3:15]
    context = {
        "post_list": posts,
    }

    model = Post


    def get_queryset(self):
        return Post.objects.select_related('category').filter(category__slug=self.kwargs.get("slug"))
    
    


####POSTDETAIL
def post_details(request, id):
    post = Post.objects.filter(id=id).first()
    if post:
            hit_count, created = HitCount.objects.get_or_create(
                post=post,
                ip=request.META.get('REMOTE_ADDR', None)
            )


    return render(request, 'blog/post_detail.html', {"post":post})


def post_search(request):
    form = PostSearchForm(request.GET)
    posts = Post.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        if search_query:
            posts = posts.filter(title__icontains=search_query)

    context = {
        'form': form,
        'posts': posts,
    }

    return render(request, 'blog/post_search.html', context)

 

def post_list(request, category=None):
    # Get unique categories from the database
    categories = Post.objects.values_list('category__name', flat=True).distinct()

    if category:
        posts = Post.objects.filter(category__name=category)
    else:
        posts = Post.objects.all()

    context = {
        'posts': posts,
        'selected_category': category,
        'categories': categories,
    }

    if request.is_ajax():
        # If the request is AJAX, return the posts data as JSON
        return JsonResponse({'html': render_to_string('posts/posts_list.html', context)})
    else:
        # If it's a regular request, render the template
        return render(request, 'posts/posts_list.html', context)