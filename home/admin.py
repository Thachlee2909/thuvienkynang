from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Post

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')

admin.site.unregister(User)  # Gỡ bản mặc định
admin.site.register(User, CustomUserAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'section', 'is_published', 'created_at')
    list_filter = ('section', 'is_published', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)
# Register your models here.
