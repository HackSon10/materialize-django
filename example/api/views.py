from rest_framework import serializers, viewsets, permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import PersonaSerializer
from ..models import Persona

class PersonaListAPIView(ListCreateAPIView):
  queryset = Persona.objects.all()
  serializer_class = PersonaSerializer
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
