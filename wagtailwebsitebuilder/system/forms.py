from django import forms

from wagtail.users.forms import UserEditForm

from .models import UserProfile


class CustomUserEditForm(UserEditForm):
    twitter_handle = forms.CharField(required=False)
    facebook_url = forms.URLField(required=False)
    linkedin_url = forms.URLField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if hasattr(self.instance, 'custom_profile'):
            profile = self.instance.custom_profile
            self.fields['twitter_handle'].initial = profile.twitter_handle
            self.fields['facebook_url'].initial = profile.facebook_url
            self.fields['linkedin_url'].initial = profile.linkedin_url
        else:
            UserProfile.objects.create(user=self.instance)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.custom_profile.twitter_handle = self.cleaned_data[
            'twitter_handle']
        user.custom_profile.facebook_url = self.cleaned_data[
            'facebook_url']
        user.custom_profile.linkedin_url = self.cleaned_data[
            'linkedin_url']

        if self.password_enabled:
            password = self.cleaned_data['password1']
            if password:
                user.set_password(password)

        if commit:
            user.save()
            self.save_m2m()
        return user
