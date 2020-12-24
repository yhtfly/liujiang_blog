# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='博客分类', max_length=128)),
            ],
            options={
                'verbose_name': '博客分类',
                'verbose_name_plural': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='博客标题', max_length=128)),
                ('img', models.ImageField(verbose_name='博客配图', blank=True, null=True, upload_to='blog_images')),
                ('body', models.TextField(verbose_name='博客正文')),
                ('abstract', models.TextField(verbose_name='博客摘要', max_length=256, blank=True, null=True)),
                ('visiting', models.PositiveIntegerField(verbose_name='博客访问量', default=0)),
                ('created_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('modified_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('author', models.ForeignKey(verbose_name='博客作者', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(verbose_name='博客分类', to='blog.Category')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客正文',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='博客标签', max_length=128)),
            ],
            options={
                'verbose_name': '博客标签',
                'verbose_name_plural': '博客标签',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(verbose_name='博客标签', to='blog.Tag'),
        ),
    ]
