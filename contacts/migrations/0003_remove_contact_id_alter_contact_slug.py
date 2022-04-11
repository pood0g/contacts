# Generated by Django 4.0.3 on 2022-04-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_delete_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AlterField(
            model_name='contact',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False, unique=True),
        ),
    ]