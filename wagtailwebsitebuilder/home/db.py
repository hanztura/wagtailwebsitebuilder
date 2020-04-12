class CSSMixin:
    @property
    def css_url(self):
        url = False
        if self.css and hasattr(self.css, 'url'):
            url = self.css.url
        return url
