from rest_framework import serializers

from epoka_projects.models import InternalProjects, Events, ExternalProjects


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class InternalProjectsSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = InternalProjects
        fields = (
            "project_title",
            "project_coordinator",
            "faculty",
            "department",
            "project_duration",
            "meeting_date",
            "link_to_official_page",
            "budget",
            "link_of_dissemination",
        )


class InternalProjectSerializerRead(InternalProjectsSerializerWrite):
    events = EventsSerializer(many=True)

    class Meta(InternalProjectsSerializerWrite.Meta):
        fields = InternalProjectsSerializerWrite.Meta.fields + ('events',)


class ExternalProjectsSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = ExternalProjects
        fields = (
            "project_title",
            "project_partner",
            "faculty",
            "department",
            "project_duration",
            "meeting_date",
            "link_to_official_page",
            "budget",
            "link_of_dissemination",
        )


class ExternalProjectsReadSerializer(ExternalProjectsSerializerWrite):
    events = EventsSerializer(many=True)

    class Meta(ExternalProjectsSerializerWrite.Meta):
        fields = ExternalProjectsSerializerWrite.Meta.fields + ('events',)
