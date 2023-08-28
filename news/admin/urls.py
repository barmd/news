from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name = "admin"),
    path('main/', views.main_menu, name = "main"),
    path('create/', views.create_post, name = "create"),
    path('user_form/', views.add_form, name = "user_form"),
]