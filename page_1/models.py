from django.db import models

# Create your models here.
class Questions(models.Model):
    """
    'question_text' or first positional param is the name of column in DB,
    'CharField' or 'DateTimeField' is the type of data in this column
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date of publication')


class Choice(models.Model):
    """ What is question???"""
    question = models.ForeignKey(
        Questions,
        on_delete=models.CASCADE,
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
