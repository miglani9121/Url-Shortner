# Generated by Django 4.0.6 on 2022-07-12 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='short_url',
            new_name='uuid',
        ),
    ]
