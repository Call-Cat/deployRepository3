# Generated by Django 4.1 on 2024-05-09 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todoitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='user',
        ),
    ]
