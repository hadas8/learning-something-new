# Generated by Django 3.0 on 2022-09-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='defsult.jpg', upload_to='book_images/'),
        ),
    ]
