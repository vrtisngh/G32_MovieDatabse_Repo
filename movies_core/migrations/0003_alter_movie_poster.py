# Generated by Django 5.2 on 2025-04-10 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_core', '0002_movielist_userprofile_favoritemovie_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
