# Generated by Django 2.2.12 on 2020-04-26 16:11

from django.db import migrations
import puputextension.helpers
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20200426_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('bash', 'Bash/Shell'), ('java', 'Java'), ('python3', 'Python 3'), ('javascript', 'Javascript'), ('css', 'CSS'), ('html', 'HTML')], null=False)), ('caption', wagtail.core.blocks.CharBlock(blank=True, nullable=True, required=False)), ('code', puputextension.helpers.CodeTextBlock())])), ('custom_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('css_class', wagtail.core.blocks.ChoiceBlock(choices=[('is-16x16', '16x16'), ('is-24x24', '24x24'), ('is-32x32', '32x32'), ('is-48x48', '48x48'), ('is-64x64', '64x64'), ('is-96x96', '96x96'), ('is-128x128', '128x128'), ('is-square', 'square'), ('is-1by1', '1by1'), ('is-5by4', '5by4'), ('is-4by3', '4by3'), ('is-3by2', '3by2'), ('is-5by3', '5by3'), ('is-16by9', '16by9'), ('is-2by1', '2by1'), ('is-3by1', '3by1'), ('is-4by5', '4by5'), ('is-3by4', '3by4'), ('is-2by3', '2by3'), ('is-3by5', '3by5'), ('is-9by16', '9by16'), ('is-1by2', '1by2'), ('is-1by3', '1by3')], required=False)), ('is_rounded', wagtail.core.blocks.BooleanBlock(required=False))])), ('hero', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('title_tag', wagtail.core.blocks.ChoiceBlock(choices=['h1', 'p', 'h2', 'h3', 'h4', 'h5', 'h6'])), ('subtitle', wagtail.core.blocks.TextBlock(required=False)), ('hero_class', wagtail.core.blocks.CharBlock(required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo', '---------', 'copy', 'cut---------', 'alignment'], 'minSpareRows': 0, 'startCols': 3, 'startRows': 3})), ('toc', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='TOC')), ('toc_items', wagtail.core.blocks.TextBlock())])), ('with_id', wagtail.core.blocks.StructBlock([('id', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], template='home/blocks/with_id.html'))]),
        ),
    ]
