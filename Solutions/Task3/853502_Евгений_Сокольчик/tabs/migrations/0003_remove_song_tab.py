# Generated by Django 3.0.5 on 2020-05-01 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0002_auto_20200501_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='tab',
        ),
    ]
