# from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer




