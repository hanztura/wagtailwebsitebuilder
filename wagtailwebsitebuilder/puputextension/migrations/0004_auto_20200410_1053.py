# Generated by Django 2.2.12 on 2020-04-10 10:53

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('puputextension', '0003_auto_20200410_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streambodyentrypage',
            name='stream_body',
            field=wagtail.core.fields.StreamField([('with_id', wagtail.core.blocks.StructBlock([('id', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], template='home/blocks/with_id.html')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'minSpareRows': 2, 'startCols': 3, 'startRows': 3})), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]),
        ),
    ]
