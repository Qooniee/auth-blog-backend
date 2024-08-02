# Generated by Django 5.0 on 2024-07-29 07:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=30, unique=True, verbose_name='uid')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post', verbose_name='サムネイル')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('content', models.TextField(verbose_name='内容')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name': '投稿',
                'verbose_name_plural': '投稿',
            },
        ),
    ]
