# Generated by Django 2.2.12 on 2020-04-10 10:39

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('puputextension', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streambodyentrypage',
            name='stream_body',
            field=wagtail.core.fields.StreamField([('with_id', wagtail.core.blocks.StructBlock([('id', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], template='home/blocks/with_id.html')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]),
        ),
    ]
