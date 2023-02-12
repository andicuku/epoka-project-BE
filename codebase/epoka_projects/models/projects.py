from django.db import models


class CommonFields(models.Model):
    project_title = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    project_duration = models.CharField(max_length=255)
    meeting_date = models.DateField()
    link_to_official_page = models.URLField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    link_of_dissemination = models.URLField(null=True, blank=True)
    events = models.ManyToManyField('Events', related_name='%(class)s', blank=True)

    class Meta:
        abstract = True


class InternalProjects(CommonFields):
    project_coordinator = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.project_title.title()} - {self.project_coordinator.title()} - {self.meeting_date}"


class ExternalProjects(CommonFields):
    project_partner = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.project_title} - {self.project_partner} - {self.meeting_date}"


class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} - ({self.start_date} - {self.end_date})"
