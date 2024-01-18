# Generated by Django 5.0.1 on 2024-01-18 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_comment_blog'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, default='guest', null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
        migrations.RemoveField(
            model_name='blog',
            name='delete_request',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='edit_request',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]