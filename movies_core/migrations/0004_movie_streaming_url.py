# Generated by Django 5.2 on 2025-04-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_core', '0003_alter_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='streaming_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
