from django.http import JsonResponse
from django.views.generic.edit import CreateView

from .forms import ContactForm as Contact, ContactFormModelForm


class ContactFormCreateView(CreateView):
    model = Contact
    form_class = ContactFormModelForm
    http_method_names = ['post']

    def get_success_url(self):
        url = self.request.META.get('HTTP_REFERER', None) or '/'
        return url

    def form_invalid(self, form):
        ajax = self.request.is_ajax()
        raise Exception
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)

        return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'ok': True
            }
            return JsonResponse(data)

        return response
