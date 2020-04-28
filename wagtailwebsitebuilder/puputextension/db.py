from puput.abstracts import BlogAbstract
from wagtailschemaorg.models import PageLDMixin

from home.db import WebContentSchemaMixin


class CustomBlogPageAbstract(
        WebContentSchemaMixin, PageLDMixin, BlogAbstract):
    class Meta:
        abstract = True
