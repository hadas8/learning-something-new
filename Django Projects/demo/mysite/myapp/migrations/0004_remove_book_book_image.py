# Generated by Django 3.0 on 2022-09-15 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220915_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_image',
        ),
    ]
