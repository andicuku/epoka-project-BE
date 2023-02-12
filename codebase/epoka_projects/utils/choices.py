from model_utils import Choices

IMPACT_FACTOR = Choices(
    (1, "WOS", "Web of Science"),
    (2, "SCOPUS", "Scopus"),
    (3, "OTHER", "Other"),
)

ConferenceType = Choices(
    (1, "CONFERENCE", "Conference"),
    (2, "SYMPOSIUM", "Symposium"),
    (3, "WORKSHOP", "Workshop"),
    (4, "SEMINAR", "Seminar"),
    (5, "COLLOQUIM", "Colloquium"),
    (6, "ROUNDTABLE", "Roundtable")
)
