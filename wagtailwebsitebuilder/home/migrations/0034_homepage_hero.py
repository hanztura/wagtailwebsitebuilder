# Generated by Django 2.2.12 on 2020-04-26 16:20

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20200426_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero',
            field=wagtail.core.fields.StreamField([('hero', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('title_tag', wagtail.core.blocks.ChoiceBlock(choices=[('h1', 'h1'), ('p', 'p'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6')])), ('subtitle', wagtail.core.blocks.TextBlock(required=False)), ('hero_class', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, null=True),
        ),
    ]