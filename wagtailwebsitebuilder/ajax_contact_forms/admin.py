from django.contrib import admin

from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'created',
        'sender_email',
        'sender_name',
        'sender_message',
        'is_sender_notified',
        'is_admin_notified',
        'from_email',
        'admin_emails',
    ]
    readonly_fields = (
        'id',
        'sender_email',
        'sender_name',
        'sender_message',
        'is_sender_notified',
        'is_admin_notified',
        'from_email',
        'admin_emails',
    )
    list_display = (
        'id',
        'created',
        'sender_email',
        'sender_message'
    )


admin.site.register(ContactForm, ContactFormAdmin)
