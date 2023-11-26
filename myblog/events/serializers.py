from rest_framework import serializers
from .models import Event, Sport


class EventSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    sports = serializers.PrimaryKeyRelatedField(queryset=Sport.objects.all(), many=True)
    description = serializers.CharField()
    location = serializers.CharField(max_length=200)
    date = serializers.DateField()
    img = serializers.ImageField()