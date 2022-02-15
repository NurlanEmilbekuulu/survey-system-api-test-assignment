from datetime import date
from uuid import uuid4

from django.db import models

from .consts import QUESTION_TYPES, TEXT


class Survey(models.Model):
    """ Survey """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    publish_date = models.DateField("Publication date", default=date.today, editable=False)
    expire_date = models.DateField("Expiration date", default=date.today)

    class Meta:
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'
        ordering = ['-publish_date']

    def __str__(self):
        return str(self.name)


class Response(models.Model):
    """
    A Response object is a collection of questions and answers with a
    unique interview uuid.
    """

    created = models.DateTimeField(verbose_name='Creation date', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Update date', auto_now=True)
    survey = models.ForeignKey(to='surveys.Survey', on_delete=models.CASCADE, related_name="responses")
    user = models.ForeignKey(to='auth.User', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'

    def __str__(self):
        return f'Response #{self.pk}'


class Question(models.Model):
    """ Question model """
    survey = models.ForeignKey(to='surveys.Survey', on_delete=models.CASCADE, related_name="questions")
    text = models.TextField(verbose_name='Text')
    type = models.CharField(verbose_name='Type', max_length=200, choices=QUESTION_TYPES, default=TEXT)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answer(models.Model):
    """ Base Answer model """
    question = models.ForeignKey(to='surveys.Question', on_delete=models.CASCADE, related_name="answers")
    response = models.ForeignKey(to='surveys.Response', on_delete=models.CASCADE, related_name="answers")
    created = models.DateTimeField(verbose_name='Creation date', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Update date', auto_now=True)
    body = models.TextField(verbose_name='Content', blank=True, null=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
