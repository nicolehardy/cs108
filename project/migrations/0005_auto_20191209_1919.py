# Generated by Django 2.2.6 on 2019-12-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20191209_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='image',
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
