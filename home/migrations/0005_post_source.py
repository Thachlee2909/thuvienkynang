# Generated by Django 5.1.7 on 2025-04-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_post_uploaded_file_post_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='source',
            field=models.CharField(blank=True, help_text='Nguồn của bài viết (nếu có)', max_length=255, null=True),
        ),
    ]
