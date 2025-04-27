from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'uploaded_file', 'video_url', 'author', 'section', 'is_published', 'category', 'source')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }