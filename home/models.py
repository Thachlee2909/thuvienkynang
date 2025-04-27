from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # Thêm import này
from django.utils.text import slugify

class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    SECTION_CHOICES = [
        ('section1', 'Kiến thức về lịch sử, địa lý, văn hoá...'),
        ('section2', 'Kiến thức về tổ chức Đoàn - Hội - Đội'),
        ('section3', 'Kiến thức về nghi thức - điều lệ'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    uploaded_file = models.FileField(upload_to='uploads/', blank=True, null=True)  # cho PDF, mp4
    video_url = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, default='section1')  # Giữ lại section
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)  # Giữ lại trạng thái publish
    source = models.CharField(max_length=255, blank=True, null=True, help_text="Nguồn của bài viết (nếu có)")
    # Thêm quan hệ với category nếu cần
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})  # Đổi 'article_detail' thành 'post_detail'
    