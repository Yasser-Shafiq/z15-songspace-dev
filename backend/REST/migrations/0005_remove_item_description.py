# Generated by Django 3.1.6 on 2021-03-08 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('REST', '0004_playlist_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
    ]
