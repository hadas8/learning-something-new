# Generated by Django 3.0 on 2022-09-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_book_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='default.jpg', upload_to='book_images/'),
        ),
    ]
