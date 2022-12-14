# Generated by Django 4.0.5 on 2022-06-14 22:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0018_remove_user_followers_user_followers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follows',
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followee', models.ManyToManyField(blank=True, related_name='followee', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
