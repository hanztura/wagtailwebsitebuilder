import uuid

from django.db import models

from django_extensions.db.models import TimeStampedModel
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmetadata.models import MetadataPageMixin
from wagtailschemaorg.models import PageLDMixin

from home.db import CSSMixin, WebContentSchemaMixin


class Instructor(TimeStampedModel):
    name = models.CharField(max_length=250)
    handle = models.CharField(max_length=250)
    email_address = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Tutorial(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=250)
    is_closed = models.BooleanField(default=False)
    short_description = models.TextField()
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.PROTECT,
        related_name='tutorials',
        null=True)

    def __str__(self):
        return self.title


class Batch(TimeStampedModel):
    tutorial = models.ForeignKey(
        Tutorial,
        on_delete=models.PROTECT,
        related_name='batches')
    enrollment_until = models.DateTimeField(blank=True, null=True)
    starts_on = models.DateField()
    enrollee_limit = models.PositiveSmallIntegerField(default=10)


class BatchEnrollee(TimeStampedModel):
    name = models.CharField(max_length=250)
    email_address = models.EmailField()
    is_paid = models.BooleanField(default=False, blank=True)


class TutorialIndexPage(
        WebContentSchemaMixin, PageLDMixin, CSSMixin, MetadataPageMixin, Page):
    css = models.FileField(
        upload_to='css/home/',
        null=True,
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('css', classname='full'),
        InlinePanel('tutorials', label='Tutorials'),
    ]

    og_type = 'website'

    promote_panels = MetadataPageMixin.promote_panels


class TutorialIndexPageTutorials(Orderable, models.Model):
    page = ParentalKey(
        'tutorials.TutorialIndexPage',
        on_delete=models.CASCADE,
        related_name='tutorials')
    tutorial = models.ForeignKey(
        'tutorials.Tutorial',
        on_delete=models.CASCADE,
        related_name='in_tutorials_page')

    panels = [
        FieldPanel('tutorial')
    ]
