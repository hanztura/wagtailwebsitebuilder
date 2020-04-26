import json
from collections import namedtuple

from wagtail.core import blocks

from .blocks import CustomImageBlock


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
