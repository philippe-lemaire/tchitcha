# Generated by Django 3.2.9 on 2021-11-11 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_showing_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=5400)),
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer_url',
            field=models.URLField(blank=True),
        ),
    ]
