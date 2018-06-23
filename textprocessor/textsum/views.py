from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import SummarizeSerializer
from django.shortcuts import render

from .services import Summarize

@api_view(['POST'])
def text_sum_viewfunction(request):
    """On POST to the API endpoint, validate the input and return the serialized summary class."""
    serializer = SummarizeSerializer(data=request.data)
    if serializer.is_valid():   # Validate input
        # Return Serializer class with original text, summary, language, sentence count, and algorithm
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # On validation error, return error and 400 status

def index_viewfunction(request):
    """Render the index page"""
    return render(request, 'textsum/index.html')
