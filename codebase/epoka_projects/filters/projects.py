import django_filters.rest_framework as filters

from epoka_projects.models import InternalProjects, ExternalProjects


class InternalProjectsFilter(filters.FilterSet):
    meeting_date_year = filters.CharFilter(method='filter_meeting_date')
    project_coordinator = filters.CharFilter(lookup_expr='icontains')
    project_title = filters.CharFilter(lookup_expr='icontains')
    faculty = filters.CharFilter(lookup_expr='icontains')
    department = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = InternalProjects
        fields = {
            'meeting_date': ['gte', 'lte', 'exact', 'icontains', 'gt', 'lt'],
            'budget': ['gte', 'lte', 'exact', 'icontains', 'gt', 'lt'],
        }

    @staticmethod
    def filter_meeting_date(queryset, name, value):
        return queryset.filter(meeting_date__year=value)


class ExternalProjectsFilter(filters.FilterSet):
    meeting_date_year = filters.CharFilter(method='filter_meeting_date')
    project_partner = filters.CharFilter(lookup_expr='icontains')
    project_title = filters.CharFilter(lookup_expr='icontains')
    faculty = filters.CharFilter(lookup_expr='icontains')
    department = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ExternalProjects
        fields = {
            'meeting_date': ['gte', 'lte', 'exact', 'icontains', 'gt', 'lt'],
            'budget': ['gte', 'lte', 'exact', 'icontains', 'gt', 'lt'],
        }

    @staticmethod
    def filter_meeting_date(queryset, name, value):
        return queryset.filter(meeting_date__year=value)
