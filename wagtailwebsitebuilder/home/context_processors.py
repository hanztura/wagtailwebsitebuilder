from django.conf import settings


def get_google_analytics(request):
    _id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', '')
    return {
        'GOOGLE_ANALYTICS_ID': _id
    }
