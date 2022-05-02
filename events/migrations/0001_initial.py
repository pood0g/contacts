# Generated by Django 4.0.3 on 2022-04-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('slug', models.SlugField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('event_start', models.DateTimeField()),
                ('event_end', models.DateTimeField()),
                ('all_day', models.BooleanField()),
                ('title', models.CharField(max_length=80)),
                ('background_color', models.CharField(choices=[('GRN', '#00FF00'), ('BLU', '#0000FF'), ('RED', '#FF0000')], max_length=3)),
            ],
            options={
                'ordering': ['event_start'],
            },
        ),
    ]
