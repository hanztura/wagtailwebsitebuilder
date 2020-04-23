# Generated by Django 2.2.12 on 2020-04-23 03:31

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('multisite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitebranding',
            name='banner_colour',
        ),
        migrations.AddField(
            model_name='sitebranding',
            name='nav_icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='sitebranding',
            name='primary_color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
    ]