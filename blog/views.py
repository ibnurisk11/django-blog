from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from .forms import PostForm  # Pastikan forms.py sudah ada

def home(request):
    return render(request, 'blog/home.html')

def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories
    })

def about(request):
    return render(request, 'blog/about.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Lebih aman dari error 404
    return render(request, 'blog/post_detail.html', {'post': post})

def create_post(request):
    if not request.user.is_authenticated:  # Pastikan user sudah login
        return redirect('login')  # Arahkan ke halaman login jika belum

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # Ambil kategori pertama yang ada (lebih aman dari hardcode id)
            default_category = Category.objects.first()  
            if default_category:
                post.category = default_category
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form})