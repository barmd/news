from django.urls import path
from . import views , context
from .views import post_search

urlpatterns = [
    #--------------Posts
    path('post-details/<int:id>/', views.post_details, name="post_single"),
    path('post-list/<slug:slug>/', views.PostListView.as_view(), name="post_list"),
    path('', views.home, name = "home"),
    path('contact/', views.ContactPageView.as_view(), name = "contact"),
    path('author/', views.author, name = "author"),
    path('lastpost/', views.TheLastpost, name = "theLastpost"),
    path('post-search/', post_search, name='post_search'),



]