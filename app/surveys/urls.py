from django.urls import path

from . import views

urlpatterns = [
    path('surveys/', views.SurveyListAPIView.as_view(), name='survey-list'),
]
