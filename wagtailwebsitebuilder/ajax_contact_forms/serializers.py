from django.conf import settings
from django.core.mail import EmailMessage

from rest_framework import serializers

from .forms import get_admin_emails_as_flat_list
from .models import ContactForm as Contact


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'sender_email',
            'sender_name',
            'sender_message',
        ]

    def is_valid(self, *args, **kwargs):
        """Set from_email and admin_emails then proceed"""

        is_valid = super().is_valid(*args, **kwargs)
        return is_valid

    def save(self, *args, **kwargs):
        """Send email to admin then save"""

        kwargs['from_email'] = settings.DEFAULT_FROM_EMAIL

        emails = get_admin_emails_as_flat_list()
        emails = ','.join(emails)  # transform to comma separated strings
        kwargs['admin_emails'] = emails

        contact = super().save(*args, **kwargs)

        mail_result = self.send_email(contact)
        if mail_result:
            contact.is_admin_notified = True
            contact.save()
        return contact

    def send_email(self, contact):
        # mail content
        email = contact.sender_email
        name = contact.sender_name
        message = contact.sender_message

        request = self.context.get('request', None)
        try:
            host = request.get_host()
        except Exception as e:
            host = str(settings.ALLOWED_HOSTS)

        referrer = getattr(request, 'META', {}).get('HTTP_REFERER', '')

        message = """
            URL: {}
            Name: {}
            Email: {}
            Message: {}
            """.format(referrer, name, email, message)
        subject = '{}: Contact Form'.format(host)
        recipient_list = contact.admin_emails_as_list

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=contact.from_email,
            to=recipient_list,
        )

        return email.send(fail_silently=True)
