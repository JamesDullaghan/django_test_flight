"""Django Models."""
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):

    """Question Class."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        """Human readable question text."""
        return self.question_text

    def was_published_recently(self):
        """Method for recently published questions."""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'


class Choice(models.Model):

    """Choice Class."""

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Human readable choice text."""
        return self.choice_text
