from blog.models import Category, Link,Post


def get_category_context(request):
    category = Category.objects.order_by('-date')[:5]
    context = {
        'category': category,
    }
    return context


def get_link_context(request):
    linkInst = Link.objects.all().order_by('-date')[:1]
    context = {
        'linkInst': linkInst,
    }
    return context
    

def get_post_details(request):
    detailPosts = Post.objects.all().order_by('-date')[4:6]
    sidebar = Post.objects.all().order_by('-date')[6:8]
    context ={
        'details': detailPosts,
        "sidebar": sidebar
    }  
    return context