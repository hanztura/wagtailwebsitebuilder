from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtailmetadata.models import MetadataPageMixin


@register_snippet
class NavBarItem(models.Model):
    link = models.CharField(max_length=250, blank=True, default='#')
    text = models.CharField(max_length=50, blank=True)

    panels = [
        FieldPanel('link'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text


class HomePageNavBarItem(Orderable, models.Model):
    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='navbar_items')
    navbar_item = models.ForeignKey(
        'home.NavBarItem',
        on_delete=models.CASCADE,
        related_name='in_home_pages')

    panels = [
        SnippetChooserPanel('navbar_item')
    ]


class HomePage(MetadataPageMixin, Page):
    body = StreamField([
        ('with_id', blocks.StructBlock(
            [
                ('id', blocks.CharBlock()),
                ('paragraph', blocks.RichTextBlock()),
            ],
            template='home/blocks/with_id.html'
        )),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock())
    ])
    navbar_icon = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('navbar_icon'),
        InlinePanel('navbar_items', label='Navbar Items'),
        StreamFieldPanel('body', classname='full'),
    ]

    promote_panels = Page.promote_panels + MetadataPageMixin.panels
