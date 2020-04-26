from wagtail.core import blocks


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
    body = blocks.RichTextBlock()
    css_class = blocks.CharBlock()

    class Meta:
        template = 'home/blocks/custom_rich_text.html'
        icon = 'doc-full'
