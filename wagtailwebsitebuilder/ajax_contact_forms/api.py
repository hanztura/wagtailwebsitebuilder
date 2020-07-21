from rest_framework import generics

from .models import ContactForm as Contact
from .serializers import ContactFormSerializer


class ContactFormApi(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = []
