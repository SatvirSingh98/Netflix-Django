# Generated by Django 3.2.4 on 2021-06-21 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_alter_video_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Videos', 'verbose_name_plural': 'All Videos'},
        ),
    ]
