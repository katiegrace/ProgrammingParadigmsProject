# Generated by Django 4.1.3 on 2022-12-06 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_post_dislikes_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='response',
            field=models.BooleanField(default=False),
        ),
    ]
