"""
    Serializers
"""

from rest_framework import serializers

from .models import Question, Answer, Survey


class AnswerSerializer(serializers.ModelSerializer):
    """ Answer model serializer """

    class Meta:
        """ pass """
        model = Answer
        fields = ['text']


class QuestionSerializer(serializers.ModelSerializer):
    """ Question model serializer """
    id = serializers.UUIDField(required=False)
    text = serializers.CharField(required=False, max_length=255)
    answer_options = AnswerSerializer(many=True, required=False)

    class Meta:
        """ pass """
        model = Question
        fields = ['id', 'text', 'answer_type', 'answer_options']


class SurveyListSerializer(serializers.HyperlinkedModelSerializer):
    """ Survey results list serializer """

    class Meta:
        """ meta """
        model = Survey
        fields = ['name', 'description', 'publish_date', 'expire_date']
