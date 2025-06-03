from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'meta_description', 'featured_image')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'meta_description', 'featured_image', 'content')
        }),
    )