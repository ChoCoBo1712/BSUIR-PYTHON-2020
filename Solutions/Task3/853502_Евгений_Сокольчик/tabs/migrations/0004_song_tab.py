# Generated by Django 3.0.5 on 2020-05-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0003_remove_song_tab'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='tab',
            field=models.CharField(default='songsterr.com', max_length=100, verbose_name='Tab'),
        ),
    ]
