from rest_framework import serializers

from epoka_projects.models import Conferences, Journal, Book


class ConferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferences
        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
