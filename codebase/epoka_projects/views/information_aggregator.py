from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from epoka_projects.filters import ConferenceFilter, JournalFilter, BookFilter
from epoka_projects.models import Conferences, Journal, Book, InternalProjects, ExternalProjects
from epoka_projects.views.projects import InternalProjectsFilter, ExternalProjectsFilter


class InformationAggregator(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def get_aggregated_information(self, request):
        response = {
            'conferences': {},
            'journals': {},
            "books": {},
            "internal_projects": {},
            "external_projects": {},
        }
        GET = request.GET
        conferences = ConferenceFilter(GET, Conferences.objects.all()).qs
        journal = JournalFilter(GET, Journal.objects.all()).qs
        books = BookFilter(GET, Book.objects.all()).qs
        internal_projects = InternalProjectsFilter(GET, InternalProjects.objects.all()).qs
        external_projects = ExternalProjectsFilter(GET, ExternalProjects.objects.all()).qs

        # group conferences by year
        for conference in conferences:
            if conference.conference_start_date.year not in response['conferences']:
                response['conferences'][conference.conference_start_date.year] = []
            response['conferences'][conference.conference_start_date.year].append(conference.__str__())

        # group journals by year
        for journal in journal:
            if journal.published_date.year not in response['journals']:
                response['journals'][journal.published_date.year] = []
            response['journals'][journal.published_date.year].append(journal.__str__())

        # group books by year
        for book in books:
            if book.published_date.year not in response['books']:
                response['books'][book.published_date.year] = []
            response['books'][book.published_date.year].append(book.__str__())

        # group internal projects by year
        for internal_project in internal_projects:
            if internal_project.meeting_date.year not in response['internal_projects']:
                response['internal_projects'][internal_project.meeting_date.year] = []
            response['internal_projects'][internal_project.meeting_date.year].append(internal_project.__str__())

        # group external projects by year
        for external_project in external_projects:
            if external_project.meeting_date.year not in response['external_projects']:
                response['external_projects'][external_project.meeting_date.year] = []
            response['external_projects'][external_project.meeting_date.year].append(external_project.__str__())

        return Response(response)
