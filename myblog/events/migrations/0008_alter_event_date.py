# Generated by Django 4.2.2 on 2023-06-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_remove_event_author_event_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='Дата проведения'),
        ),
    ]
