from django import forms
from django.conf import settings
from django.core.mail import EmailMessage

from .models import ContactForm


def get_admin_emails_as_flat_list():
    emails = settings.ADMINS
    emails = [email for name, email in emails]
    return emails


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = [
            'sender_email',
            'sender_name',
            'sender_message',
        ]

    def is_valid(self):
        """Set from_email and admin_emails then proceed"""
        from_email = 'webmaster@xofytech.com'  # TODO
        self.instance.from_email = from_email

        emails = get_admin_emails_as_flat_list()
        emails = ','.join(emails)  # transform to comma separated strings
        self.instance.admin_emails = emails

        is_valid = super().is_valid()
        return is_valid

    def save(self, commit=False):
        """Send email to admin then save"""
        mail_result = self.send_email()
        if mail_result:
            self.instance.is_admin_notified = True

        contact = super().save(commit=commit)

        return contact

    def send_email(self):
        # mail content
        contact = self.instance
        email = contact.sender_email
        name = contact.sender_name
        message = contact.sender_message
        message = '\
            Name: {}\
            Email: {}\
            Message: {}\
            '.format(name, email, message)
        subject = 'Contact Form'
        recipient_list = contact.admin_emails_as_list

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=contact.from_email,
            to=recipient_list,
        )

        return email.send(fail_silently=True)
