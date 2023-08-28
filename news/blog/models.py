from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from datetime import datetime, date
from django.urls import reverse



class User(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    password = models.TextField(max_length=50)
    notes = models.TextField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    date = models.DateField(("Date"), auto_now_add=True)


    def __str__(self):
        return self.name



class Category(MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    notes = models.TextField(max_length=250)
    date = models.DateField(("Date"), auto_now_add=True)
    parent = TreeForeignKey(
        'self',
        related_name = 'childer',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    class MPTTMeta:
        order_Insertion_by = ['name']

    def __str__(self):
        return self.name    


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    # order = models.IntegerField(null=True)

    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True
    )
    date = models.DateField(auto_now_add=False)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_single', kwargs={"slug":self.category.slug, "post_slug":self.slug})
    
    slug = models.SlugField(max_length=200)
    
    @property
    def hit_count(self):
        return HitCount.objects.filter(post_id=self.id).count()


class HitCount(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.CharField(max_length=30)
    date = models.DateField(("Date"), auto_now_add=True)

         
class SideBar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    video = models.FileField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(
        Category, 
        related_name="posts",
        on_delete=models.SET_NULL,
        null=True
        )
    date = models.DateField(auto_now_add=False)
    
    def __str__(self):
        return self.title
    

class ArticlesList(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(("Date"), auto_now_add=True)


class UsersView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(("Date"), auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.TextField(max_length=50)
    subject = models.TextField(max_length=250)
    message = models.TextField()


    def __str__(self):
        return self.name
 

