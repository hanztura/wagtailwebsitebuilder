from django.urls import path

from .api import ContactFormApi


app_name = 'ajax_contact_forms'
urlpatterns = [
    path('simple', ContactFormApi.as_view(), name='simple')
]
