# Generated by Django 3.2.9 on 2022-11-25 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20221124_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userss',
            name='user_post_name',
        ),
    ]
