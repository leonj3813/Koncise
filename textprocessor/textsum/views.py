from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import SummarizeSerializer

from .services import Summarize

@api_view(['POST'])
def text_sum_viewfunction(request):
    serializer = SummarizeSerializer(data=request.data)
    if serializer.is_valid():
        summarizer = SummarizeSerializer(serializer.save())
        return Response(summarizer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
