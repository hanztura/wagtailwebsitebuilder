from django.db import models

from modelcluster.fields import ParentalKey
from puput.models import EntryPage, BlogPage
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, InlinePanel,
    PageChooserPanel, StreamFieldPanel)
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from .helpers import CodeBlock
from home.db import CSSMixin


class CustomBlogPageNavBarItem(Orderable, models.Model):
    page = ParentalKey(
        'puputextension.CustomBlogPage',
        on_delete=models.CASCADE,
        related_name='navbar_items')
    navbar_item = models.ForeignKey(
        'home.NavBarItem',
        on_delete=models.CASCADE,
        related_name='in_custom_blog_pages')

    panels = [
        SnippetChooserPanel('navbar_item')
    ]


class CustomBlogPage(BlogPage):
    content_panels = BlogPage.content_panels + [
        InlinePanel('navbar_items', label='Navbar Items'),
    ]


class StreamBodyEntryPage(
        CSSMixin,
        EntryPage):
    stream_body = StreamField([
        ('with_id', blocks.StructBlock(
            [
                ('id', blocks.CharBlock()),
                ('paragraph', blocks.RichTextBlock()),
            ],
            template='home/blocks/with_id.html'
        )),
        ('table', TableBlock(table_options={
            'minSpareRows': 0,
            'startRows': 3,
            'startCols': 3,
            'contextMenu': [
                'row_above',
                'row_below',
                '---------',
                'col_left',
                'col_right',
                '---------',
                'remove_row',
                'remove_col',
                '---------',
                'undo',
                'redo',
                '---------',
                'copy',
                'cut'
                '---------',
                'alignment',
            ],
        })),
        ('paragraph', blocks.RichTextBlock()),
        ('code', CodeBlock()),
        ('image', ImageChooserBlock())
    ])
    css = models.FileField(
        upload_to='css/puput/entry_page/',
        null=True,
        blank=True)

    content_panels = [
        StreamFieldPanel('stream_body', classname="full"),
        MultiFieldPanel(
            [
                FieldPanel('css', classname='full'),
                FieldPanel('title', classname="title"),
                ImageChooserPanel('header_image'),
                FieldPanel('excerpt', classname="full"),
                FieldPanel('body', classname="full"),
            ],
            heading="Content"
        ),
        MultiFieldPanel(
            [
                FieldPanel('tags'),
                InlinePanel('entry_categories', label="Categories"),
                InlinePanel(
                    'related_entrypage_from',
                    label="Related Entries",
                    panels=[PageChooserPanel('entrypage_to')]
                ),
            ],
            heading="Metadata"),
    ]


BlogPage.subpage_types.append(StreamBodyEntryPage)
