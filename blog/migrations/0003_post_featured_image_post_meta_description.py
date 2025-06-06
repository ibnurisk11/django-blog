# Generated by Django 5.2.1 on 2025-06-03 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Deskripsi untuk SEO (maks 160 karakter)', max_length=160),
        ),
    ]
