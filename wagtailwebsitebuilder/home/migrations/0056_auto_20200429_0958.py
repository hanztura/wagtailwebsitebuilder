# Generated by Django 2.2.12 on 2020-04-29 09:58

from django.db import migrations
import puputextension.helpers
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_auto_20200429_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('card', wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('css_class', wagtail.core.blocks.ChoiceBlock(choices=[('is-16x16', '16x16'), ('is-24x24', '24x24'), ('is-32x32', '32x32'), ('is-48x48', '48x48'), ('is-64x64', '64x64'), ('is-96x96', '96x96'), ('is-128x128', '128x128'), ('is-square', 'square'), ('is-1by1', '1by1'), ('is-5by4', '5by4'), ('is-4by3', '4by3'), ('is-3by2', '3by2'), ('is-5by3', '5by3'), ('is-16by9', '16by9'), ('is-2by1', '2by1'), ('is-3by1', '3by1'), ('is-4by5', '4by5'), ('is-3by4', '3by4'), ('is-2by3', '2by3'), ('is-3by5', '3by5'), ('is-9by16', '9by16'), ('is-1by2', '1by2'), ('is-1by3', '1by3')], required=False)), ('is_rounded', wagtail.core.blocks.BooleanBlock(required=False))], required=False)), ('content', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=False)), ('css_class', wagtail.core.blocks.CharBlock(required=False))])), ('html', wagtail.core.blocks.RawHTMLBlock())])), ('css_class', wagtail.core.blocks.CharBlock(required=False))])), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('bash', 'Bash/Shell'), ('java', 'Java'), ('python3', 'Python 3'), ('javascript', 'Javascript'), ('css', 'CSS'), ('html', 'HTML')], null=False)), ('caption', wagtail.core.blocks.CharBlock(blank=True, nullable=True, required=False)), ('code', puputextension.helpers.CodeTextBlock())])), ('columns', wagtail.core.blocks.StructBlock([('columns', wagtail.core.blocks.StreamBlock([('column', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('css_class', wagtail.core.blocks.ChoiceBlock(choices=[('is-16x16', '16x16'), ('is-24x24', '24x24'), ('is-32x32', '32x32'), ('is-48x48', '48x48'), ('is-64x64', '64x64'), ('is-96x96', '96x96'), ('is-128x128', '128x128'), ('is-square', 'square'), ('is-1by1', '1by1'), ('is-5by4', '5by4'), ('is-4by3', '4by3'), ('is-3by2', '3by2'), ('is-5by3', '5by3'), ('is-16by9', '16by9'), ('is-2by1', '2by1'), ('is-3by1', '3by1'), ('is-4by5', '4by5'), ('is-3by4', '3by4'), ('is-2by3', '2by3'), ('is-3by5', '3by5'), ('is-9by16', '9by16'), ('is-1by2', '1by2'), ('is-1by3', '1by3')], required=False)), ('is_rounded', wagtail.core.blocks.BooleanBlock(required=False))], required=False)), ('content', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=False)), ('css_class', wagtail.core.blocks.CharBlock(required=False))])), ('html', wagtail.core.blocks.RawHTMLBlock())])), ('css_class', wagtail.core.blocks.CharBlock(required=False))])), ('html', wagtail.core.blocks.RawHTMLBlock()), ('paragraph', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=False)), ('css_class', wagtail.core.blocks.CharBlock(required=False))]))])), ('css_class', wagtail.core.blocks.CharBlock(required=False))]))])), ('css_class', wagtail.core.blocks.CharBlock(required=False)), ('container_tag', wagtail.core.blocks.ChoiceBlock(choices=[('article', 'article'), ('div', 'div'), ('nav', 'nav'), ('section', 'section')]))])), ('custom_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('css_class', wagtail.core.blocks.ChoiceBlock(choices=[('is-16x16', '16x16'), ('is-24x24', '24x24'), ('is-32x32', '32x32'), ('is-48x48', '48x48'), ('is-64x64', '64x64'), ('is-96x96', '96x96'), ('is-128x128', '128x128'), ('is-square', 'square'), ('is-1by1', '1by1'), ('is-5by4', '5by4'), ('is-4by3', '4by3'), ('is-3by2', '3by2'), ('is-5by3', '5by3'), ('is-16by9', '16by9'), ('is-2by1', '2by1'), ('is-3by1', '3by1'), ('is-4by5', '4by5'), ('is-3by4', '3by4'), ('is-2by3', '2by3'), ('is-3by5', '3by5'), ('is-9by16', '9by16'), ('is-1by2', '1by2'), ('is-1by3', '1by3')], required=False)), ('is_rounded', wagtail.core.blocks.BooleanBlock(required=False))])), ('custom_paragraph', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=False)), ('css_class', wagtail.core.blocks.CharBlock(required=False))])), ('html', wagtail.core.blocks.RawHTMLBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('schema_product', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock(default='', required=False)), ('audience_type', wagtail.core.blocks.CharBlock(default='', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('schema_person', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock(default='', required=False)), ('email', wagtail.core.blocks.EmailBlock(default='', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo', '---------', 'copy', 'cut---------', 'alignment'], 'minSpareRows': 0, 'startCols': 3, 'startRows': 3})), ('tile', wagtail.core.blocks.StreamBlock([('tile', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('css_class', wagtail.core.blocks.ChoiceBlock(choices=[('is-16x16', '16x16'), ('is-24x24', '24x24'), ('is-32x32', '32x32'), ('is-48x48', '48x48'), ('is-64x64', '64x64'), ('is-96x96', '96x96'), ('is-128x128', '128x128'), ('is-square', 'square'), ('is-1by1', '1by1'), ('is-5by4', '5by4'), ('is-4by3', '4by3'), ('is-3by2', '3by2'), ('is-5by3', '5by3'), ('is-16by9', '16by9'), ('is-2by1', '2by1'), ('is-3by1', '3by1'), ('is-4by5', '4by5'), ('is-3by4', '3by4'), ('is-2by3', '2by3'), ('is-3by5', '3by5'), ('is-9by16', '9by16'), ('is-1by2', '1by2'), ('is-1by3', '1by3')], required=False)), ('is_rounded', wagtail.core.blocks.BooleanBlock(required=False))], required=False)), ('body', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=False)), ('css_class', wagtail.core.blocks.CharBlock(required=False))], required=False)), ('css_class', wagtail.core.blocks.CharBlock(required=False)), ('html', wagtail.core.blocks.RawHTMLBlock(required=False))]))])), ('toc', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='TOC')), ('toc_items', wagtail.core.blocks.TextBlock())])), ('with_id', wagtail.core.blocks.StructBlock([('id', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], template='home/blocks/with_id.html'))]),
        ),
    ]
