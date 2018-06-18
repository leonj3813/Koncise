from rest_framework import serializers
from .services import Summarize

class SummarizeSerializer(serializers.Serializer):
    language = serializers.CharField(required=False)
    sentences_count = serializers.IntegerField(required=False)
    summary = serializers.CharField(required=False)
    text = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Summarize` instance, given the validated data.
        """
        return Summarize(**validated_data)
