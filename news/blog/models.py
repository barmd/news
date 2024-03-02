from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from datetime import datetime, date
from django.urls import reverse
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from django.contrib.auth import get_user


class Category(MPTTModel):
    user = models.ForeignKey(
        User, 
        on_delete=models.
        CASCADE
        )
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

class Tag(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(("Date"), auto_now_add=True)

    def __str__(self):
        return self.name    

class Post(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.
        CASCADE
        )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    content = models.TextField()
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Bir nechat avriantni tanlang: ',
        blank=False,
    )
    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True
    )
    date = models.DateField(("Date"), auto_now_add=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_single', kwargs={"slug":self.category.slug, "post_slug":self.slug})
    
    slug = models.SlugField(max_length=200)
    
    
    def hit_count(self):
        return HitCount.objects.filter(post_id=self.id).count()
    

class HitCount(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.CharField(max_length=30)
    date = models.DateField(("Date"), auto_now_add=True)


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    site = models.TextField(max_length=200)
    text = models.TextField(max_length=800)

    def __str__(self):
        return self.name

class Icon(models.Model):
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Link(models.Model):
    colorcode = ColorField(default='#FF0000')
    icon = models.ForeignKey(
        Icon,
        verbose_name='Ikonka tanlang: ',
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(max_length=100)
    url = models.TextField(max_length=400)
    date = models.DateField(auto_now_add=True, null=True, blank=True)



class ArticlesList(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(("Date"), auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.TextField(max_length=50)
    subject = models.TextField(max_length=250)
    message = models.TextField()
    date = models.DateField(("Date"), auto_now_add=True)



    def __str__(self):
        return self.name
 
