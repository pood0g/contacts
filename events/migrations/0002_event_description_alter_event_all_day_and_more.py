# Generated by Django 4.0.3 on 2022-05-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='all_day',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='background_color',
            field=models.CharField(choices=[('GRN', '#00FF00'), ('RED', '#FF0000'), ('BLU', '#0000FF')], max_length=3),
        ),
    ]
