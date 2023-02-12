import django_filters.rest_framework as filters
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from epoka_projects.filters import InternalProjectsFilter, ExternalProjectsFilter
from epoka_projects.models import InternalProjects as InternalProjectsModel, ExternalProjects as ExternalProjectsModel, \
    Events
from epoka_projects.serializers import InternalProjectsSerializerWrite, InternalProjectSerializerRead, \
    ExternalProjectsSerializerWrite, EventsSerializer


class CommonProjectsView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    read_serializer = None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.read_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.read_serializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(request=EventsSerializer, responses=EventsSerializer)
    @action(detail=True, methods=['post'])
    def add_event(self, request, pk=None):
        event_data = EventsSerializer(data=request.data)
        event_data.is_valid(raise_exception=True)
        validated_data = event_data.validated_data
        events = Events.objects.create(**validated_data)
        self.get_object().events.add(events)
        return Response(EventsSerializer(events).data)

    @extend_schema(request=EventsSerializer, responses=EventsSerializer)
    @action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        events = self.get_object().events.all()
        return Response(EventsSerializer(events, many=True).data)

    @extend_schema(request=EventsSerializer, responses=EventsSerializer)
    @action(detail=False, methods=['delete'])
    def delete_event(self, request, pk=None):
        event = Events.objects.get(pk=request.data['event_id'])
        event.delete()
        return Response(EventsSerializer(event).data)

    @extend_schema(request=EventsSerializer, responses=EventsSerializer)
    @action(detail=False, methods=['put'])
    def update_event(self, request, pk=None):
        event = Events.objects.get(pk=request.data['event_id'])
        event_data = EventsSerializer(data=request.data)
        event_data.is_valid(raise_exception=True)
        validated_data = event_data.validated_data
        event = Events.objects.filter(pk=event.id).update(**validated_data)
        event.save()
        return Response(EventsSerializer(event).data)


class InternalProjectsView(CommonProjectsView):
    queryset = InternalProjectsModel.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = InternalProjectsFilter
    serializer_class = InternalProjectsSerializerWrite
    read_serializer = InternalProjectSerializerRead


class ExternalProjectsView(CommonProjectsView):
    queryset = ExternalProjectsModel.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ExternalProjectsFilter
    serializer_class = ExternalProjectsSerializerWrite
    read_serializer = InternalProjectSerializerRead
