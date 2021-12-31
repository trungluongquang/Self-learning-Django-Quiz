from django.db import models
from lib.slug import generate_slug
from django.forms import ValidationError

"""
Manage all questions
"""


class Question(models.Model):
    question = models.TextField()


def validate_topic_name(topic_name: str):
    """
    check if the topic name already exists in the database for `QuestionTopic`. If yes, `ValidationError` is thrown
    :param topic_name:
    :return:
    """
    topic_name = str(topic_name).strip()
    if len(QuestionTopic.objects.filter(topic__iexact=topic_name)) > 0:
        raise ValidationError([{'topic': 'This topic has been used'}])


class QuestionTopic(models.Model):
    topic = models.CharField(max_length=255, validators=[validate_topic_name])
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
    icon = models.ImageField(upload_to='topic_icon/')

    def save(self, *args, **kwargs):
        self.topic = str(self.topic).strip()
        self.slug = str(self.slug).strip()
        if not self.slug:
            self.slug = generate_slug(input_text=self.topic, filter_obj=QuestionTopic)
        super(QuestionTopic, self).save(*args, **kwargs)

