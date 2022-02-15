from datetime import datetime

from django.db.models import Q
from rest_framework import viewsets, mixins, permissions
from rest_framework.generics import get_object_or_404

from .models import Survey, Question, Answer, Choice
from .serializers import (
    SurveySerializer, QuestionSerializer, AnswerSerializer,
    UserSurveySerializer, AnswerOneTextSerializer,
    AnswerOneChoiceSerializer, AnswerMultipleChoiceSerializer,
    ChoiceSerializer,
)


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (permissions.IsAdminUser,)


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        survey = get_object_or_404(Survey, id=self.kwargs['id'])
        return survey.questions.all()

    def perform_create(self, serializer):
        survey = get_object_or_404(Survey, pk=self.kwargs['id'])
        serializer.save(survey=survey)


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = (permissions.IsAdminUser,)

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            survey__id=self.kwargs['id'],
        )
        serializer.save(question=question)

    def get_queryset(self):
        question = get_object_or_404(Question, id=self.kwargs['question_pk'])
        return question.choices.all()


class ActiveSurveyListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Survey.objects.filter(expire_date__gte=datetime.today())
    serializer_class = SurveySerializer
    permission_classes = (permissions.AllowAny,)


class AnswerCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            survey__id=self.kwargs['id'],
        )

        if question.question_type == 'text':
            return AnswerOneTextSerializer
        elif question.question_type == 'single':
            return AnswerOneChoiceSerializer
        else:
            return AnswerMultipleChoiceSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            survey__id=self.kwargs['id'],
        )
        serializer.save(author=self.request.user, question=question)


class UserIDSurveyListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSurveySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Survey.objects.exclude(~Q(questions__answers__author__id=user_id))
        return queryset
