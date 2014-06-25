from django.db import models


# Create your models here.

class Grammar(models.Model):
  nick = models.CharField('Nick name',max_length=200)
  question_1st = models.CharField('First part of question',max_length=200)
  question_2nd = models.CharField('Second part of question',max_length=200)
  pub_date = models.DateTimeField('date published')
  def __unicode__(self):
    return self.nick

class Choice(models.Model):
  parent = models.ForeignKey(Grammar)
  choice_text = models.CharField(max_length=200)
  is_correct = models.BooleanField('This is the correct answer')
  def __unicode__(self):
    return self.choice_text
