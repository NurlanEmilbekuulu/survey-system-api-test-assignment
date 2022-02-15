from datetime import date

from rest_framework import generics

from .models import Survey
from .serializers import SurveyListSerializer


class SurveyListAPIView(generics.ListAPIView):
    """API endpoint для просмотра списка опросов участником"""
    serializer_class = SurveyListSerializer
    queryset = Survey.objects.filter(expire_date__gte=date.today())
