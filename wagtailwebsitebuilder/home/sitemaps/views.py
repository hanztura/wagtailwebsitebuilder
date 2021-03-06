import inspect
from django.contrib.sitemaps import (
    views as sitemap_views, Sitemap as DjangoSitemap)


class Sitemap(DjangoSitemap):

    def __init__(self, request=None):
        self.request = request

    def location(self, obj):
        return obj.get_full_url(self.request)

    def lastmod(self, obj):
        # fall back on latest_revision_created_at if last_published_at is null
        # (for backwards compatibility from before last_published_at was added)
        last_mod = obj.last_published_at or obj.latest_revision_created_at
        last_mod = last_mod.strftime('%Y-%m-%dT%H:%M:%S%z')
        return last_mod

    def get_wagtail_site(self):
        site = getattr(self.request, 'site', None)
        if site is None:
            from wagtail.core.models import Site
            return Site.objects.select_related(
                'root_page'
            ).get(is_default_site=True)
        return site

    def items(self):
        return (
            self.get_wagtail_site()
            .root_page
            .get_descendants(inclusive=True)
            .live()
            .public()
            .order_by('path')
            .specific())

    def _urls(self, page, protocol, domain):
        urls = []
        last_mods = set()

        for item in self.paginator.page(page).object_list:

            url_info_items = item.get_sitemap_urls(self.request)

            for url_info in url_info_items:
                urls.append(url_info)
                last_mods.add(url_info.get('lastmod'))

        # last_mods might be empty if the whole site is private
        if last_mods and None not in last_mods:
            self.latest_lastmod = max(last_mods)
        return urls


def index(request, sitemaps, **kwargs):
    sitemaps = prepare_sitemaps(request, sitemaps)
    return sitemap_views.index(request, sitemaps, **kwargs)


def sitemap(request, sitemaps=None, **kwargs):
    if sitemaps:
        sitemaps = prepare_sitemaps(request, sitemaps)
    else:
        sitemaps = {'wagtail': Sitemap(request)}
    return sitemap_views.sitemap(request, sitemaps, **kwargs)


def prepare_sitemaps(request, sitemaps):
    """Intialize the wagtail Sitemap by passing the request.site value. """
    initialised_sitemaps = {}
    for name, sitemap_cls in sitemaps.items():
        if inspect.isclass(sitemap_cls) and issubclass(sitemap_cls, Sitemap):
            initialised_sitemaps[name] = sitemap_cls(request)
        else:
            initialised_sitemaps[name] = sitemap_cls
    return initialised_sitemaps
