# Generated by Django 4.2.2 on 2023-06-27 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='write_date',
        ),
        migrations.RemoveField(
            model_name='review',
            name='writer',
        ),
    ]
