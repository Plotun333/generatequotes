from django.db import models
import datetime
from django.utils import timezone



class Question(models.Model):
    Quote_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    posquote = models.CharField(default='', max_length=200)


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class BEST(models.Model):
    best = models.CharField(max_length=200)






