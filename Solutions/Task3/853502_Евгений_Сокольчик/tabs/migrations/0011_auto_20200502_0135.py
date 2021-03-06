# Generated by Django 3.0.5 on 2020-05-01 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0010_auto_20200502_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='url',
            field=models.SlugField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='guitarist',
            name='url',
            field=models.SlugField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='url',
            field=models.SlugField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='url',
            field=models.SlugField(default='1', max_length=100),
        ),
    ]
