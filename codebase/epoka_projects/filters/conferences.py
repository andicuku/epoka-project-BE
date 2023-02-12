import django_filters.rest_framework as filters

from epoka_projects.models import Conferences, Book, Journal
from epoka_projects.utils.choices import ConferenceType


class ConferenceFilter(filters.FilterSet):
    conference_type = filters.ChoiceFilter(choices=ConferenceType)
    conference_name = filters.CharFilter(lookup_expr='icontains')
    conference_start_date_year = filters.CharFilter(method='filter_conference_start_date_year')
    conference_end_date_year = filters.CharFilter(method='filter_conference_end_date')
    conference_location = filters.CharFilter(lookup_expr='icontains')
    conference_organizer = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Conferences
        fields = {
            'conference_start_date': ['lte', 'gte', 'exact', 'gt', 'lt'],
            'conference_end_date': ['lte', 'gte', 'exact', 'gt', 'lt'],
        }

    @staticmethod
    def filter_conference_start_date_year(queryset, name, value):
        return queryset.filter(conference_start_date__year=value)

    @staticmethod
    def filter_conference_end_date(queryset, name, value):
        return queryset.filter(conference_end_date__year=value)


class JournalFilter(filters.FilterSet):
    author = filters.CharFilter(lookup_expr='icontains')
    journal_title = filters.CharFilter(lookup_expr='icontains')
    faculty = filters.CharFilter(lookup_expr='icontains')
    department = filters.CharFilter(lookup_expr='icontains')
    published_date_year = filters.CharFilter(method='filter_published_date_year')

    @staticmethod
    def filter_published_date_year(queryset, name, value):
        return queryset.filter(published_date__year=value)

    class Meta:
        model = Journal
        fields = {
            'published_date': ["gte", "gt", "lt", "lte", "range"],
        }


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(lookup_expr='icontains')
    book_title = filters.CharFilter(lookup_expr='icontains')
    faculty = filters.CharFilter(lookup_expr='icontains')
    department = filters.CharFilter(lookup_expr='icontains')
    published_company = filters.CharFilter(lookup_expr='icontains')
    published_date_year = filters.CharFilter(method='filter_published_date_year')

    class Meta:
        model = Book
        fields = {
            'published_date': ["gte", "gt", "lt", "lte", "range"],
        }

    @staticmethod
    def filter_published_date_year(queryset, name, value):
        return queryset.filter(published_date__year=value)
