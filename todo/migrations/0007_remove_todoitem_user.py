# Generated by Django 4.1 on 2024-05-09 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_todoitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='user',
        ),
    ]
