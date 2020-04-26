from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


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
