from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    author = serializers.CharField(max_length=100)
    date = serializers.DateField()
    img = serializers.ImageField()

