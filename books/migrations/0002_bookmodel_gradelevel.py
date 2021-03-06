# Generated by Django 3.1.6 on 2021-02-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='GradeLevel',
            field=models.CharField(blank=True, choices=[('K-2', 'K-2'), ('3-5', '3-5'), ('6-8', '6-8'), ('9-12', '9-12'), ('Young Adult', 'Young Adult')], default='6-8', max_length=20, null=True, verbose_name='Grade Level of this book (Default is 6-8)'),
        ),
    ]
