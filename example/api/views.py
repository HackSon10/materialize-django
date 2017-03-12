import django_filters
from rest_framework import serializers, viewsets, permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import PersonaSerializer
from ..models import Persona

# class PersonaFilter(django_filters.rest_framework.FilterSet):
#   class Meta:
#     model = Persona
#     fields = ['nombre', 'edad', 'correo']

class PersonaListAPIView(ListCreateAPIView):
  queryset = Persona.objects.all()
  serializer_class = PersonaSerializer
  filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
  filter_fields = ['nombre', 'edad', 'correo']
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
