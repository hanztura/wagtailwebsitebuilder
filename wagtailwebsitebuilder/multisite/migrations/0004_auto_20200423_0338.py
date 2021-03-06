# Generated by Django 2.2.12 on 2020-04-23 03:38

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('multisite', '0003_sitebranding_banner_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitebranding',
            name='accent_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='sitebranding',
            name='fav_icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='sitebranding',
            name='secondary_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='sitebranding',
            name='text_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AlterField(
            model_name='sitebranding',
            name='primary_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]
