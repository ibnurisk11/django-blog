from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),  # Ganti 'index' dengan 'home' sesuai dengan views.py
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
]