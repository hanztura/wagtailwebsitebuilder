import os

from django.conf import settings
from django.http import FileResponse

from .models import SeoSettings


def robots(request):
    robots_text = SeoSettings.for_site(request.site).robots_txt

    if robots_text:
        return FileResponse(robots_text.file)
    else:
        filename = os.path.join(settings.MEDIA_ROOT, 'robots.txt')
        if not os.path.isfile(filename):
            with open(filename, 'w') as fp:
                default = """User-agent: *
Disallow: /cms/
Disallow: /admin/"""
                fp.write(default)
        return FileResponse(open(filename, 'rb'))
