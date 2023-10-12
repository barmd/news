from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic import TemplateView
from blog.forms import ContactForm
from blog.models import Post, HitCount, Category
from django.http import HttpResponse

###HOME

def home(request):
    posts = Post.objects.all().order_by('-date')[3:15]
    top_post = Post.objects.all().order_by('-date')[:1]
    top_post_two = Post.objects.all().order_by('-date')[1:2]
    top_post_three = Post.objects.all().order_by('-date')[2:3]
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

    # def get(self, request, *args, **kwargs):
    #     form = ContactForm()
    #     form.save()
    #     context = {
    #         'form': form
    #     }

    #     return render(request, 'blog/contact.html', context)

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
    postes = Post.objects.all().order_by('-date')[:15]
    context = {
        "last_post": postes,
    }

    return render(request, 'blog/theLastpost.html', context)


###Post list

class PostListView(ListView):
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





 