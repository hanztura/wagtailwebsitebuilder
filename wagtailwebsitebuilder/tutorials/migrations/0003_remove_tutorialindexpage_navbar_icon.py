# Generated by Django 2.2.15 on 2020-09-05 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_tutorialindexpage_tutorialindexpagetutorials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialindexpage',
            name='navbar_icon',
        ),
    ]
