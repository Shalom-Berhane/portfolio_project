# Generated by Django 3.0.5 on 2020-04-30 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200430_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
    ]