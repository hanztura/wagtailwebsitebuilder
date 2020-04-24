import json
from collections import namedtuple

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data):
    try:
        return json.loads(data, object_hook=_json_object_hook)
    except Exception as e:
        return None


class TocBlock(blocks.StructBlock):
    title = blocks.CharBlock(default='TOC')
    toc_items = blocks.TextBlock()

    class Meta:
        template = 'home/blocks/toc.html'
        icon = 'list-ul'

    @property
    def items(self):
        return json2obj(self.toc_items)


IMAGE_CLASS_CHOICES = (
    ('is-16x16', '16x16'),
    ('is-24x24', '24x24'),
    ('is-32x32', '32x32'),
    ('is-48x48', '48x48'),
    ('is-64x64', '64x64'),
    ('is-96x96', '96x96'),
    ('is-128x128', '128x128'),
    ('is-square', 'square'),
    ('is-1by1', '1by1'),
    ('is-5by4', '5by4'),
    ('is-4by3', '4by3'),
    ('is-3by2', '3by2'),
    ('is-5by3', '5by3'),
    ('is-16by9', '16by9'),
    ('is-2by1', '2by1'),
    ('is-3by1', '3by1'),
    ('is-4by5', '4by5'),
    ('is-3by4', '3by4'),
    ('is-2by3', '2by3'),
    ('is-3by5', '3by5'),
    ('is-9by16', '9by16'),
    ('is-1by2', '1by2'),
    ('is-1by3', '1by3'),
)


class CustomImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    css_class = blocks.ChoiceBlock(
        choices=IMAGE_CLASS_CHOICES,
        required=False)
    is_rounded = blocks.BooleanBlock(required=False)

    class Meta:
        template = 'home/blocks/image.html'
        icon = 'image'
