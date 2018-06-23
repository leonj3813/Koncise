from rest_framework import serializers
from textsum.services import Summarize

class SummarizeSerializer(serializers.Serializer):
    """
    Serializer for the text summarizer.

    Fields: text (required), language, sentences_count, algorithm, summary.
    """
    language = serializers.CharField(required=False)
    sentences_count = serializers.IntegerField(required=False)
    summary = serializers.CharField(required=False)
    algorithm = serializers.CharField(required=False)
    text = serializers.CharField()

    def validate_algorithm(self, value):
        """Validate that the algorithm input is one of the accepted values 'lsa', 'lexrank', or 'textrank'"""
        if value.lower() not in ['lsa', 'lexrank', 'textrank']:
            raise serializers.ValidationError("{} is not a valid choice.".format(value))
        return value

    def create(self, validated_data):
        """
        Create and return a new `Summarize` instance, given the validated data. The summary of the text field
        is in the summary property.
        """
        return Summarize(**validated_data)
