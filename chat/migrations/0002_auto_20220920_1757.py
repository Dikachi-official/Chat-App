# Generated by Django 2.1 on 2022-09-20 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='info',
            new_name='value',
        ),
    ]
