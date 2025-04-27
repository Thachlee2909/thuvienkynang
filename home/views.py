from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm  # Đã đổi từ ArticleForm sang PostForm
from .models import Post  # Đã đổi từ Article sang Post
from django.http import HttpResponseForbidden
from django.utils.text import slugify


def home(request):
    """View function for home page"""
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Xin chào {username}!")
                return redirect('home')  # Thay 'home' bằng tên URL trang chủ của bạn
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.info(request, "Bạn đã đăng xuất thành công.")
    return redirect('home')  # Thay 'home' bằng tên URL trang chủ của bạn

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Đăng ký thành công!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required  # Yêu cầu đăng nhập để truy cập
def dashboard(request):
    """Trang dashboard sau khi đăng nhập"""
    return render(request, 'home/dashboard.html', {
        'user': request.user  # Truyền thông tin user vào template
    })
    
def kienthuc_view(request):
    return render(request, 'kienthuc.html')

def leutrai_view(request):
    return render(request, 'leutrai.html')

def matthu_view(request):
    return render(request, 'matthu.html')

def morse_view(request):
    return render(request, 'morse.html')

def muahat_view(request):
    return render(request, 'muahat.html')

def nghithucdoi_view(request):
    return render(request, 'nghithucdoi.html')

def nghithuchoi_view(request):
    return render(request, 'nghithuchoi.html')


def nutday_view(request):
    return render(request, 'nutday.html')

def phuonghuong_view(request):
    return render(request, 'phuonghuong.html')

def scc_view(request):
    return render(request, 'scc.html')

def semaphore_view(request):
    return render(request, 'semaphore.html')

def thoathiem_view(request):
    return render(request, 'thoathiem.html')

def thuocnam_view(request):
    return render(request, 'thuocnam.html')

def thuoctay_view(request):
    return render(request, 'thuoctay.html')

def trochoi_view(request):
    return render(request, 'trochoi.html')

def uocdat_view(request):
    return render(request, 'uocdat.html')

def kienthuc(request):
    sections = {
        'section1': {
            'title': 'Kiến thức về lịch sử, địch lý, văn hoá, xã hội, tình hình kinh tế - chính trị của đất nước',
            'posts': Post.objects.filter(section='section1', is_published=True)
        },
        'section2': {
            'title': 'Kiến thức về tổ chức Đoàn - Hội - Đội',
            'posts': Post.objects.filter(section='section2', is_published=True)
        },
        'section3': {
            'title': 'Kiến thức về nghi thức - điều lệ',
            'posts': Post.objects.filter(section='section3', is_published=True)
        }
    }
    
    return render(request, 'kienthuc.html', {'sections': sections})

@login_required
def create_post(request):  # Đổi tên từ create_article sang create_post
    # Kiểm tra quyền - chỉ cho phép staff hoặc superuser đăng bài
    if not (request.user.is_staff or request.user.is_superuser):
        return HttpResponseForbidden("Bạn không có quyền đăng bài")
    
    if request.method == 'POST':
        form = PostForm(request.POST)  # Đổi từ ArticleForm sang PostForm
        if form.is_valid():
            post = form.save(commit=False)  # Đổi từ article sang post
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect('kienthuc')
    else:
        form = PostForm()  # Đổi từ ArticleForm sang PostForm
    
    return render(request, 'create_post.html', {'form': form})  # Đổi template name

def post_detail(request, slug):  # Đổi từ article_detail sang post_detail
    post = get_object_or_404(Post, slug=slug, is_published=True)  # Đổi từ Article sang Post
    return render(request, 'post_detail.html', {'post': post})  # Đổi template name và biến

@login_required
def edit_post(request, slug):  # Đổi tên từ edit_article sang edit_post
    post = get_object_or_404(Post, slug=slug)  # Đổi từ Article sang Post
    
    # Kiểm tra quyền: chỉ tác giả hoặc staff/superuser mới được chỉnh sửa
    if post.author != request.user and not (request.user.is_staff or request.user.is_superuser):
        return HttpResponseForbidden("Bạn không có quyền chỉnh sửa bài viết này")
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # Đổi từ ArticleForm sang PostForm
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)  # Đổi tên view
    else:
        form = PostForm(instance=post)  # Đổi từ ArticleForm sang PostForm
    
    return render(request, 'edit_post.html', {'form': form, 'post': post})  # Đổi template name và biến

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'home/post_list.html', {'posts': posts})

# Xóa các hàm trùng lặp và không sử dụng
# - Xóa hàm create_article trùng lặp
# - Xóa hàm create_post cũ (nếu không dùng)
# - Xóa hàm post_detail cũ (dùng id thay vì slug)
