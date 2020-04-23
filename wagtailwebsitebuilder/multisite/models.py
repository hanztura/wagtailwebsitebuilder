from __future__ import absolute_import, unicode_literals

from django.db import models

from colorfield.fields import ColorField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, PageChooserPanel, MultiFieldPanel)
from wagtail.contrib.settings.models import BaseSetting, register_setting

# The LinkFields and RelatedLink meta-models
# are taken from the WagtailDemoimplementation.
# They provide a multi-field panel that allows you
# to set a link title and choose either
# an internal or external link. It also provides a
# custom property ('link') to simplify
# using it in the template.


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete="models.CASCADE",
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True


class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


@register_setting
class SocialMediaSettings(BaseSetting):
    """The SocialMediaSettings model provides site-specific social media links.
    These could be easily expanded to include any number of social media
    URLs / IDs.
    """
    facebook = models.URLField(
        help_text='Your Facebook page URL',
        null=True,
        blank=True
    )
    twitter = models.CharField(
        max_length=255,
        help_text='Your Twitter username, without the @',
        null=True,
        blank=True
    )


@register_setting
class FooterLinks(BaseSetting, ClusterableModel):
    """The FooterLinks model takes advantage of the RelatedLink model we
    implemented above.
    """

    panels = [
        InlinePanel('footer_links', label="Footer Links"),
    ]


class FooterLinksRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('FooterLinks', related_name='footer_links')


@register_setting
class SiteBranding(BaseSetting):
    """RE the SiteBranding model, you'll note that there's no
    custom-validation on the
    banner_colour field to check that a valid hex value has been
    entered. This would
    probably be better off as a select field with a set of predefined
    colour choices.
    """
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    fav_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    nav_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    primary_color = ColorField(default='#000000')
    secondary_color = ColorField(default='#000000')
    accent_color = ColorField(default='#000000')
    accent_2_color = ColorField(default='#000000')
    banner_colour = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        help_text="Fill in a hex colour value"
    )
    css = models.FileField(
        upload_to='css/sites/',
        null=True,
        blank=True)

    panels = [
        MultiFieldPanel(
            (
                ImageChooserPanel('site_logo'),
                ImageChooserPanel('fav_icon'),
                ImageChooserPanel('nav_icon'),
            ),
            'Site Logos'
        ),
        MultiFieldPanel(
            (
                FieldPanel('primary_color'),
                FieldPanel('secondary_color'),
                FieldPanel('accent_color'),
                FieldPanel('accent_2_color'),
            ),
            'Color Palette',
        ),
        FieldPanel('css'),
    ]