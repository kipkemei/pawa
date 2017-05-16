# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 10:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=50, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Short Bio')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
                ('dob', models.DateField(blank=True, null=True)),
                ('residence', models.CharField(blank=True, max_length=50, null=True)),
                ('id_no', models.IntegerField(blank=True, null=True, verbose_name='National ID no')),
                ('phone', models.PositiveIntegerField(blank=True, null=True, verbose_name='Phone number')),
                ('address', models.CharField(blank=True, max_length=80, null=True, verbose_name='Your postal address')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Profile picture')),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_profile',
            },
        ),
    ]
