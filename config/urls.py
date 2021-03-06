from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from puput import urls as puput_urls

from search import views as search_views
from home.sitemaps.views import sitemap
from multisite.views import robots

urlpatterns = [
    path('sitemap.xml', sitemap),
    path('robots.txt', robots),

    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path(
        'cms/',
        include('admin_honeypot.urls', namespace='admin_honeypot_cms')),

    path(settings.DJANGO_ADMIN_URL, admin.site.urls),
    path(settings.WAGTAIL_CMS_URL, include(wagtailadmin_urls)),
    path('grappelli/', include('grappelli.urls')),
    path('documents/', include(wagtaildocs_urls)),

    path('search/', search_views.search, name='search'),

    path('ajax-contact-forms/', include('ajax_contact_forms.urls')),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

urlpatterns += [
#     # For anything not caught by a more specific rule above, hand over to
#     # Wagtail's page serving mechanism. This should be the last pattern in
#     # the list:

    path("", include(puput_urls)),
    path("", include(wagtail_urls)),

#     # Alternatively, if you want Wagtail pages to be served from a subpath
#     # of your site, rather than the site root:
#     #    url(r"^pages/", include(wagtail_urls)),
]
