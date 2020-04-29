from django.db import models


class SocialMediaAbstractModel(models.Model):
    twitter_handle = models.CharField(max_length=50, blank=True)
    facebook_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    class Meta:
        abstract = True

    @property
    def twitter_url(self):
        if self.twitter_handle:
            return 'https://twitter.com/' + self.twitter_handle
        else:
            return ''
