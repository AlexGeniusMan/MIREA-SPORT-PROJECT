from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('header', 'shortDescription', 'sport')


class CurrentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('header', 'fullDescription', 'sport')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('header', 'shortDescription', 'sport', 'status')


class CurrentEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('header', 'fullDescription', 'sport', 'status')
