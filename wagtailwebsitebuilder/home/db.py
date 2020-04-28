from .schemas import WebContent, Thing
from multisite.models import Organisation


class CSSMixin:
    @property
    def css_url(self):
        url = False
        if self.css and hasattr(self.css, 'url'):
            url = self.css.url
        return url


class WebContentSchemaMixin:

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
            name=self.title,
            description=about.description,
            url=about.url
        )
        return web_content.as_python_dict
