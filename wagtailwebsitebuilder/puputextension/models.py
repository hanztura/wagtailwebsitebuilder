from puput.models import EntryPage, BlogPage
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, InlinePanel,
    PageChooserPanel, StreamFieldPanel)


class StreamBodyEntryPage(EntryPage):
    stream_body = StreamField([
        ('with_id', blocks.StructBlock(
            [
                ('id', blocks.CharBlock()),
                ('paragraph', blocks.RichTextBlock()),
            ],
            template='home/blocks/with_id.html'
        )),
        ('table', TableBlock(table_options={
            'minSpareRows': 2,
            'startRows': 3,
            'startCols': 3
        })),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock())
    ])

    content_panels = [
        StreamFieldPanel('stream_body', classname="full"),
        MultiFieldPanel(
            [
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
