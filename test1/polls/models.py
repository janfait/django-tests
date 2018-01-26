import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# model corresponds to a database model with variables representing different columns 
# def ... are functions or methods attached to the model, like automated variables
# a self method will then be implemented as question.question_text for the Question model
#the models object is a collection of classes used in definition.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text


