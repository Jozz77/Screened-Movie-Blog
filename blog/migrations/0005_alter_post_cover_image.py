# Generated by Django 4.1.1 on 2022-10-14 08:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_youtube_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
