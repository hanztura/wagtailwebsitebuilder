# Generated by Django 2.2.12 on 2020-04-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multisite', '0005_auto_20200423_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitebranding',
            name='css',
            field=models.FileField(blank=True, null=True, upload_to='css/sites/'),
        ),
    ]
