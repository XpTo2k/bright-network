# Generated by Django 4.0.5 on 2022-06-08 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_comments_created_comments_edited_ideas_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='picture',
        ),
    ]
