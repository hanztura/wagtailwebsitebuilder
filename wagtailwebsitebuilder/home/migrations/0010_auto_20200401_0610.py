# Generated by Django 3.0.4 on 2020-04-01 06:10

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200401_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('with_id', wagtail.core.blocks.StructBlock([('id', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], template='home/blocs/with_id.html')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]),
        ),
    ]
