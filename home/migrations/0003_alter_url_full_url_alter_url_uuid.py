# Generated by Django 4.0.6 on 2022-07-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_short_url_url_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='full_url',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.CharField(max_length=20),
        ),
    ]