from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, StreamFieldPanel)
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.contrib.sitemaps.sitemap_generator import Sitemap
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtailmetadata.models import MetadataPageMixin
from wagtailschemaorg.models import PageLDMixin
from wagtailschemaorg.utils import extend

from .db import CSSMixin
from .blocks import (
    HeroBlock, CustomRichTextBlock, TileStreamBlock, ColumnsBlock, CardBlock)
from .helpers import TocBlock, CustomImageBlock
from .schemas import WebContent, Thing, Person
from multisite.models import Organisation
from puputextension.helpers import CodeBlock


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


class HomePage(PageLDMixin, CSSMixin, MetadataPageMixin, Page):
    hero = StreamField([
        ('hero', HeroBlock()),
    ], null=True, blank=True)
    body = StreamField([
        ('card', CardBlock()),
        ('code', CodeBlock()),
        ('columns', ColumnsBlock()),
        ('custom_image', CustomImageBlock()),
        ('custom_paragraph', CustomRichTextBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('image', ImageChooserBlock()),
        ('paragraph', blocks.RichTextBlock()),
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
        ('tile', TileStreamBlock()),
        ('toc', TocBlock()),
        ('with_id', blocks.StructBlock(
            [
                ('id', blocks.CharBlock()),
                ('paragraph', blocks.RichTextBlock()),
            ],
            template='home/blocks/with_id.html'
        )),
    ])
    navbar_icon = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True)
    css = models.FileField(
        upload_to='css/home/',
        null=True,
        blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('navbar_icon'),
        InlinePanel('navbar_items', label='Navbar Items'),
        FieldPanel('css', classname='full'),
        StreamFieldPanel('hero', classname='full'),
        StreamFieldPanel('body', classname='full'),
    ]

    promote_panels = Page.promote_panels + MetadataPageMixin.panels

    def ld_entity(self):
        site = self.get_site()
        about = Thing(
            name=self.title,
            description=self.search_description,
            url=self.get_url(),
        )
        org = Organisation.for_site(site)
        web_content = WebContent(
            about=about,
            author=org.schema,
            date_published=str(self.first_published_at),
            date_modified=str(self.last_published_at),
            text=str(self.body),
            name=self.title,
            description=about.description,
            url=about.url
        )
        return web_content.as_python_dict


class SitemapPage(MetadataPageMixin, Page):
    hero = StreamField([
        ('hero', HeroBlock()),
    ], null=True, blank=True)
    body = StreamField([
        ('custom_paragraph', CustomRichTextBlock()),
        ('html', blocks.RawHTMLBlock()),
    ])
    navbar_icon = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('navbar_icon'),
        StreamFieldPanel('hero', classname='full'),
        StreamFieldPanel('body', classname='full'),
    ]

    promote_panels = Page.promote_panels + MetadataPageMixin.panels

    def get_context(self, request):
        context = super().get_context(request)
        context['root_page'] = Sitemap(request).items().first()
        return context
