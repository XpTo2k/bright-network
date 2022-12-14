# Generated by Django 4.0.5 on 2022-06-14 22:10

from tokenize import blank_re
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from sqlalchemy import null


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_alter_user_followers_alter_user_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='follows',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='followee', to=settings.AUTH_USER_MODEL),
        ),
    ]
