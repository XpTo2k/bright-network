# Generated by Django 4.0.5 on 2022-06-14 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0022_remove_followers_user_followers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
