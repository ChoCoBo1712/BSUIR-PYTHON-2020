# Generated by Django 3.0.5 on 2020-05-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0007_remove_guitar_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='url',
            field=models.SlugField(default='1', max_length=100),
        ),
    ]
