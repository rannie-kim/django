from django.contrib import admin
from .models import Post, Like

# Register your models here.

admin.site.register(Post)  # 추가
admin.site.register(Like)