from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .services import Summarize

@api_view(['POST'])
def text_sum_viewfunction(request):
    summary = Summarize()
    #sum = Summarize.return_summary(request.data['text'])
    summary.return_summary(request.data['text'])
    print(summary.summary)
    return Response({'summary' : summary.summary})
