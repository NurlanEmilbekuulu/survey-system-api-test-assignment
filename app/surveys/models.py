from datetime import date
from uuid import uuid4

from django.db import models

from .consts import QUESTION_TYPES, TEXT


class Survey(models.Model):
    """ Survey """
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


class Question(models.Model):
    """ Question model """
    survey = models.ForeignKey(to='surveys.Survey', on_delete=models.CASCADE, related_name="questions")
    text = models.TextField(verbose_name='Text')
    question_type = models.CharField(verbose_name='Question type', max_length=200, choices=QUESTION_TYPES, default=TEXT)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Choice(models.Model):
    """ Choice model """
    text = models.TextField(verbose_name='Answer option')
    question = models.ForeignKey(
        to='surveys.Question',
        on_delete=models.CASCADE,
        related_name='choices'
    )

    def __str__(self):
        return str(self.text)


class Answer(models.Model):
    """ Answer model """
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(to='surveys.Question', on_delete=models.CASCADE, related_name="answers")
    multiple_choice = models.ManyToManyField(Choice)
    single_choice = models.ForeignKey(
        Choice,
        null=True,
        on_delete=models.CASCADE,
        related_name="answers_single_choice"
    )
    text = models.TextField(null=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
