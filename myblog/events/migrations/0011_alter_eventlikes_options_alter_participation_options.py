# Generated by Django 4.2.2 on 2024-01-11 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventlikes',
            options={'verbose_name': 'Лайк', 'verbose_name_plural': 'Лайки'},
        ),
        migrations.AlterModelOptions(
            name='participation',
            options={'verbose_name': 'Событие - виды спорта', 'verbose_name_plural': 'Событие - виды спорта'},
        ),
    ]