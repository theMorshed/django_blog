from django.contrib import admin
from blog.models import BlogModel

# Register your models here.
@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'description']