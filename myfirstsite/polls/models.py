from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Questions(models.Model):
    user = models.ForeignKey('auth.user', related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', blank=True, default=datetime.datetime.now())

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s' % (self.choice_text, self.votes)
