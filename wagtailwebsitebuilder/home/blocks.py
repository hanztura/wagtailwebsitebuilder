from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from .schemas import ITEM_TYPES_AS_CHOICES
from puputextension.helpers import CodeBlock


class HeroBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    title_tag = blocks.ChoiceBlock(
        default='h1',
        choices=(
            ('h1', 'h1'),
            ('p', 'p'),
            ('h2', 'h2'),
            ('h3', 'h3'),
            ('h4', 'h4'),
            ('h5', 'h5'),
            ('h6', 'h6'),
        )
    )
    subtitle = blocks.TextBlock(required=False)
    hero_class = blocks.CharBlock(required=False)
    cta_text = blocks.CharBlock(required=False)
    cta_href = blocks.CharBlock(required=False, default='#')
    background_image = ImageChooserBlock(required=False)

    class Meta:
        template = 'home/blocks/hero.html'


class CustomRichTextBlock(blocks.StructBlock):
    body = blocks.RichTextBlock(required=False)
    css_class = blocks.CharBlock(required=False)

    class Meta:
        template = 'home/blocks/custom_rich_text.html'
        icon = 'doc-full'


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
    image = ImageChooserBlock(required=False)
    css_class = blocks.ChoiceBlock(
        choices=IMAGE_CLASS_CHOICES,
        required=False)
    is_rounded = blocks.BooleanBlock(required=False)

    class Meta:
        template = 'home/blocks/image.html'
        icon = 'image'


class TileItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    subtitle = blocks.CharBlock(required=False)
    image = CustomImageBlock(required=False)
    body = CustomRichTextBlock(required=False)
    css_class = blocks.CharBlock(required=False)
    html = blocks.RawHTMLBlock(required=False)

    class Meta:
        template = 'home/blocks/tile_item.html'


class TileStreamBlock(blocks.StreamBlock):
    tile = TileItemBlock()

    class Meta:
        template = 'home/blocks/tile.html'


class CardBlock(blocks.StructBlock):
    image = CustomImageBlock(required=False)
    content = blocks.StreamBlock(
        [
            ('paragraph', CustomRichTextBlock()),
            ('html', blocks.RawHTMLBlock()),
        ]
    )
    css_class = blocks.CharBlock(required=False)

    class Meta:
        template = 'home/blocks/card.html'


class ColumnBlock(blocks.StructBlock):
    body = blocks.StreamBlock(
        [
            ('card', CardBlock()),
            ('html', blocks.RawHTMLBlock()),
            ('paragraph', CustomRichTextBlock()),
        ]
    )
    css_class = blocks.CharBlock(required=False)

    class Meta:
        template = 'home/blocks/column.html'


class ColumnsBlock(blocks.StructBlock):
    columns = blocks.StreamBlock(
        [
            ('column', ColumnBlock())
        ]
    )
    css_class = blocks.CharBlock(required=False)
    container_tag = blocks.ChoiceBlock(
        default='section',
        choices=(
            ('article', 'article'),
            ('div', 'div'),
            ('nav', 'nav'),
            ('section', 'section'),
        ))

    class Meta:
        template = 'home/blocks/columns.html'


class SectionBlock(blocks.StreamBlock):
    card = CardBlock(required=False)
    code = CodeBlock(required=False)
    columns = ColumnsBlock(required=False)
    image = CustomImageBlock(required=False)
    richtext = CustomRichTextBlock(required=False)
    tiles = TileStreamBlock(required=False)

    class Meta:
        template = 'home/blocks/section.html'


class SchemaPersonBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    description = blocks.CharBlock(required=False, default='')
    email = blocks.EmailBlock(required=False, default='')
    image = ImageChooserBlock(required=False)
    url = blocks.PageChooserBlock(required=False)

    class Meta:
        template = 'home/blocks/schemas/person.html'


class SchemaProductBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    description = blocks.CharBlock(required=False, default='')
    audience_type = blocks.CharBlock(required=False, default='')
    price = blocks.CharBlock()
    price_currency = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    url = blocks.PageChooserBlock(required=False)

    class Meta:
        template = 'home/blocks/schemas/product.html'
