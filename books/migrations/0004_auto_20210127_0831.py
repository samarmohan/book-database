# Generated by Django 3.1.2 on 2021-01-27 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_bookresponse_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookresponse',
            old_name='Summary',
            new_name='Description',
        ),
    ]