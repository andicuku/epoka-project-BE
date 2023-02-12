from rest_framework import routers

from epoka_projects.views import ConferencesView, JournalView, BookView, InternalProjectsView, ExternalProjectsView, \
    InformationAggregator

router = routers.SimpleRouter()
router.register(r"conferences", ConferencesView, basename="conferences")
router.register(r"journal", JournalView, basename="journal")
router.register(r"book", BookView, basename="journal")
router.register(r"internal-projects", InternalProjectsView, basename="internal-projects")
router.register(r"external-projects", ExternalProjectsView, basename="external-projects")

router.register(r"information-aggregator", InformationAggregator, basename="information-aggregator")

urlpatterns = router.urls
