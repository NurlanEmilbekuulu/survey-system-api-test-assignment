"""
    Serializers
"""
from django.db.models import Q
from rest_framework import serializers

from .models import Question, Answer, Survey, Choice


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['name', 'description', 'publish_date', 'expire_date']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'name']


class QuestionSerializer(serializers.ModelSerializer):
    """ Question model serializer """

    class Meta:
        """ pass """
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    """ Answer model serializer """

    class Meta:
        """ pass """
        model = Answer
        fields = '__all__'


class QuestionListSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField('get_answers')

    class Meta:
        fields = ['text', 'answers']
        model = Question

    def get_answers(self, question):
        # author_id = self.context.get('request').parser_context['kwargs']['id']
        author_id = self.context.get('request').user.id
        answers = Answer.objects.filter(
            Q(question=question) & Q(author__id=author_id))
        serializer = AnswerSerializer(instance=answers, many=True)
        return serializer.data


class UserSurveySerializer(serializers.ModelSerializer):
    questions = QuestionListSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Survey


class AnswerOneTextSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['text']
        model = Answer


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        question_id = self.context.get('request').parser_context['kwargs'][
            'question_pk']
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField,
                         self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(question_id=question_id)


class AnswerOneChoiceSerializer(serializers.ModelSerializer):
    one_choice = UserFilteredPrimaryKeyRelatedField(
        many=False,
        queryset=Choice.objects.all()
    )

    class Meta:
        fields = ['single_choice']
        model = Answer


class AnswerMultipleChoiceSerializer(serializers.ModelSerializer):
    many_choice = UserFilteredPrimaryKeyRelatedField(
        many=True,
        queryset=Choice.objects.all()
    )

    class Meta:
        fields = ['many_choice']
        model = Answer
