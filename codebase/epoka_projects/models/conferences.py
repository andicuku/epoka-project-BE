from django.db import models

from epoka_projects.utils.choices import IMPACT_FACTOR, ConferenceType


class Conferences(models.Model):
    conference_type = models.IntegerField(choices=ConferenceType, default=1)
    conference_name = models.CharField(max_length=255)
    conference_start_date = models.DateField()
    conference_end_date = models.DateField()
    conference_location = models.CharField(max_length=255, null=True, blank=True)
    conference_organizer = models.CharField(max_length=255, null=True, blank=True)
    participant_name = models.CharField(max_length=255, null=True)
    paper_info = models.TextField(null=True)
    link_published = models.URLField(null=True, blank=True)
    link_of_dissemination = models.URLField(null=True, blank=True)
    nationality_or_international = models.CharField(null=True, max_length=50)

    def __str__(self):
        return f"{self.conference_name.title()} - ({self.conference_start_date} - {self.conference_end_date}) - " \
               f"{self.conference_organizer.title()}"


class Journal(models.Model):
    journal_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    issn = models.CharField(max_length=255)
    doi = models.CharField(max_length=255)
    published_date = models.DateField()
    published_place = models.CharField(max_length=255)
    impactor_factor = models.PositiveSmallIntegerField(choices=IMPACT_FACTOR)
    link_published = models.URLField(null=True, blank=True)
    doi_journal = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.author.title()} - {self.published_date} - {self.journal_title.title()}"


class Book(models.Model):
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    published_date = models.DateField()
    published_company = models.CharField(max_length=255)
    link_published = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.author.title()} - {self.published_date} - {self.book_title.title()}"
