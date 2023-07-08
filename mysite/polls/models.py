import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    """
    The question of which can be answered
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """It is published recently if created within a day"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """
    The choice for each question which can be voted also.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
