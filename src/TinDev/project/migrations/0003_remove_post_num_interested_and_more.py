# Generated by Django 4.1.3 on 2022-12-02 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_post_description_alter_post_preferred_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='num_interested',
        ),
        migrations.AlterField(
            model_name='post',
            name='expiration_date',
            field=models.DateTimeField(),
        ),
    ]