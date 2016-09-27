# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='图片名称')),
                ('image', models.ImageField(upload_to='images/%Y%m')),
                ('caption', models.CharField(blank=True, max_length=250, null=True, verbose_name='图片说明')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': '图片库',
                'ordering': ['title'],
                'verbose_name': '图片库',
            },
        ),
        migrations.DeleteModel(
            name='IMG',
        ),
    ]
