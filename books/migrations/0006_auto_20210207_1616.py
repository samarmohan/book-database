# Generated by Django 3.1.6 on 2021-02-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210127_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='ContainsBadWords',
            field=models.BooleanField(blank=True, null=True, verbose_name='Is this book inappropriate for someone around 8 years old?'),
        ),
    ]