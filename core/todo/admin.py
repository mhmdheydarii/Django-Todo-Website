from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date']
    search_fields = ['title',]

admin.site.register(Post, PostAdmin)