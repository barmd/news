from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from blog.models import Post, HitCount, SideBar

def admin(request):
    return render(request, 'admin/main/login.html')

def main_menu(request):
    return render(request, 'admin/main/index.html')

def create_post(request):
    return render(request, 'admin/main/create_post.html')    


def add_form(request):
    return render(request, 'admin/main/add_user.html') 
