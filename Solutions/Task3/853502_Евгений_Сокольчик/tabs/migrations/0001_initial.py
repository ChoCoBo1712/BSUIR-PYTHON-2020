# Generated by Django 3.0.5 on 2020-05-01 18:09

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Genre')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Guitar')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Guitar',
                'verbose_name_plural': 'Guitars',
            },
        ),
        migrations.CreateModel(
            name='Guitarist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Guitarist')),
                ('age', models.PositiveSmallIntegerField(default=18, verbose_name='Age')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Guitarist',
                'verbose_name_plural': 'Guitarists',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Manufacturer')),
                ('description', models.TextField(verbose_name='Description')),
                ('logo', models.ImageField(default='manufacturer_logos/logo.png', upload_to='manufacturer_logos/', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Song')),
                ('author', models.CharField(default='Author', max_length=100, verbose_name='Author')),
                ('lyrics', models.TextField(verbose_name='Lyrics')),
                ('song', embed_video.fields.EmbedVideoField(verbose_name='Song')),
                ('tabs', models.CharField(max_length=100, verbose_name='Tabs URL')),
                ('genres', models.ManyToManyField(to='tabs.Genre', verbose_name='Genres')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
        migrations.CreateModel(
            name='GuitarPictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Guitar Picture')),
                ('image', models.ImageField(upload_to='guitar_pictures/', verbose_name='Image')),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tabs.Guitar', verbose_name='Guitar')),
            ],
            options={
                'verbose_name': 'Guitar Picture',
                'verbose_name_plural': 'Guitar Pictures',
            },
        ),
        migrations.CreateModel(
            name='GuitaristPictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Guitarist Picture')),
                ('image', models.ImageField(upload_to='guitarist_pictures/', verbose_name='Image')),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tabs.Guitarist', verbose_name='Guitarist')),
            ],
            options={
                'verbose_name': 'Guitarist Picture',
                'verbose_name_plural': 'Guitarist Pictures',
            },
        ),
        migrations.AddField(
            model_name='guitar',
            name='guitarists',
            field=models.ManyToManyField(to='tabs.Guitarist', verbose_name='Guitarists'),
        ),
        migrations.AddField(
            model_name='guitar',
            name='manufacturer',
            field=models.ManyToManyField(to='tabs.Manufacturer', verbose_name='Manufacturer'),
        ),
    ]
