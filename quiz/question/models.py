from django.db import models
from lib.slug import generate_slug
from django.template.defaultfilters import truncatechars


class QuestionTopic(models.Model):
    """
    topics for questions
    """
    topic = models.CharField(max_length=255, unique=True)
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


def _get_topic_choices():
    result = list()
    topics = QuestionTopic.objects.all()
    for topic in topics:
        result.append((topic.topic, topic.topic))
    return tuple(result)


class Question(models.Model):
    """
    questions
    """
    question = models.TextField()
    topic = models.CharField(max_length=255, choices=_get_topic_choices(), default='Allgemein')
    slug = models.SlugField(blank=True)
    correct_answer = models.CharField(max_length=255)
    wrong_answer_1 = models.CharField(max_length=255)
    wrong_answer_2 = models.CharField(max_length=255, blank=True, null=True)
    wrong_answer_3 = models.CharField(max_length=255, blank=True, null=True)
    explanation = models.TextField(blank=True)
    explanation_source = models.TextField(blank=True)
    note = models.TextField(blank=True)
    image = models.ImageField(upload_to='question_image/', blank=True)

    def save(self, *args, **kwargs):
        self.question = str(self.question).strip()
        self.slug = str(self.slug).strip()
        self.correct_answer = str(self.correct_answer).strip()
        self.wrong_answer_1 = str(self.wrong_answer_1).strip()
        self.wrong_answer_2 = str(self.wrong_answer_2).strip()
        self.wrong_answer_3 = str(self.wrong_answer_3).strip()
        self.explanation = str(self.explanation).strip()
        self.explanation_source = str(self.explanation_source).strip()
        self.note = str(self.note).strip()
        if not self.slug:
            self.slug = generate_slug(input_text=self.question, filter_obj=Question)
        super(Question, self).save(*args, **kwargs)

    @property
    def short_explanation(self):
        return truncatechars(self.explanation, 100)

