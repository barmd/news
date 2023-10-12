from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from blog.models import Post, Category, User, Contact, Link
from django.utils.html import format_html


@admin.register(Post)
class NewsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50px" height="50px" style="border-radius: 10px;" />'.format(object.image.url))
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'thumbnail', 'title']
    list_display_links = ['id', 'thumbnail', 'title']    


@admin.register(Category)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name'] 


@admin.register(User)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name'] 


@admin.register(Contact)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name'] 


@admin.register(Link)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name','url']
    list_display_links = [ 'name','url']