# Generated by Django 4.1.2 on 2022-12-02 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_remove_post_num_interested_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='recruiter',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.recruiterprofile'),
        ),
    ]
