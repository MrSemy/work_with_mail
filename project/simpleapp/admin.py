from django.contrib import admin
from .models import Author, Post, Comment, PostCategory, Category, Subscribers


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(Category)
admin.site.register(Subscribers)
# Register your models here.
