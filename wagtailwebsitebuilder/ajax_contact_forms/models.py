from django.db import models

from django_extensions.db.models import TimeStampedModel


class ContactForm(TimeStampedModel):
    sender_email = models.EmailField(blank=True)
    sender_name = models.CharField(max_length=250, blank=True)
    sender_message = models.CharField(max_length=250, blank=True)
    is_sender_notified = models.BooleanField(default=False, blank=True)
    is_admin_notified = models.BooleanField(default=False, blank=True)

    # the email info seen by admin
    from_email = models.EmailField()
    admin_emails = models.TextField()  # comma separated emails

    @property
    def admin_emails_as_list(self):
        emails = self.admin_emails.split(',')
        emails = [e.strip() for e in emails]
        return emails
