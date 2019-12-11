# Generated by Django 2.2.6 on 2019-12-11 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dance', models.TextField()),
                ('description', models.TextField()),
                ('video', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venuename', models.TextField()),
                ('streetname', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('zipcode', models.TextField(blank=True)),
                ('image', models.URLField()),
                ('website', models.URLField(blank=True)),
                ('handicap', models.TextField()),
                ('wifi', models.TextField()),
                ('coatcheck', models.TextField()),
                ('food', models.TextField()),
                ('parkinggarage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.TextField()),
                ('date', models.DateField()),
                ('date_time', models.TimeField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('image', models.URLField(blank=True)),
                ('dances', models.ManyToManyField(to='project.Dance')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Venue')),
            ],
        ),
    ]