import datetime
from django.db import models
from django.utils import timezone


class Questions(models.Model):
    """
    'question_text' or first positional param is the name of column in DB,
    'CharField' or 'DateTimeField' is the type of data in this column
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date of publication')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """ What is question???"""
    question = models.ForeignKey(
        Questions,
        on_delete=models.CASCADE,
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
