# Generated by Django 3.2.4 on 2021-06-24 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0008_auto_20210624_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVShowProxy',
            fields=[
            ],
            options={
                'verbose_name': 'TV Show',
                'verbose_name_plural': 'TV Shows',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('playlists.playlist',),
        ),
        migrations.CreateModel(
            name='TVShowSeasonProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('playlists.playlist',),
        ),
    ]
