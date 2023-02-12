import django_filters.rest_framework as filters
from rest_framework import viewsets

from epoka_projects.filters import ConferenceFilter, JournalFilter, BookFilter
from epoka_projects.models import Conferences as ConferencesModel, Journal as JournalModel, Book as BookModel
from epoka_projects.serializers.conferences import ConferencesSerializer, JournalSerializer, BookSerializer


class ConferencesView(viewsets.ModelViewSet):
    queryset = ConferencesModel.objects.all()
    serializer_class = ConferencesSerializer
    filterset_class = ConferenceFilter
    filter_backends = [filters.DjangoFilterBackend]


class JournalView(viewsets.ModelViewSet):
    queryset = JournalModel.objects.all()
    serializer_class = JournalSerializer
    filterset_class = JournalFilter
    filter_backends = [filters.DjangoFilterBackend]


class BookView(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
