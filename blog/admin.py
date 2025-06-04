from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from .models import Category, Post

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'meta_description', 'featured_image', 'author')
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'slug',
                'meta_description',
                'featured_image',
                'content',
                'category',
                'author',
            )
        }),
    )