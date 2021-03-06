# Generated by Django 3.1.6 on 2021-02-14 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, verbose_name='Your FULL name')),
                ('Email', models.EmailField(max_length=255, verbose_name='Your PERSONAL email')),
                ('Title', models.CharField(max_length=255, unique=True, verbose_name='Title of the book')),
                ('Author', models.CharField(max_length=255, verbose_name='Author of the book')),
                ('Description', models.TextField(blank=True, null=True, verbose_name='Summary of the book (Optional)')),
                ('PageCount', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of pages in the book (Optional)')),
                ('Rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Rating out of 10')),
            ],
        ),
    ]
