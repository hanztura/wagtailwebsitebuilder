from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import ContactForm as Contact
from .serializers import ContactFormSerializer


class ContactFormApi(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
