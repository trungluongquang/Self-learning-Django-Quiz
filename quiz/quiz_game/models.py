from django.db import models
from lib.slug import generate_slug
from question.models import Question
from django.forms import ValidationError


class QuizGame(models.Model):
    title = models.TextField()
    description = models.TextField()
    short_description = models.TextField(blank=True, max_length=500)
    slug = models.SlugField(blank=True)
    slug_question_1 = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='question_1')
    slug_question_2 = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='question_2')
    slug_question_3 = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='question_3')
    slug_question_4 = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='question_4')
    slug_question_5 = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='question_5')
    slug_question_6 = models.ForeignKey(Question, on_delete=models.PROTECT, blank=True, null=True,
                                        related_name='question_6')
    slug_question_7 = models.ForeignKey(Question, on_delete=models.PROTECT, blank=True, null=True,
                                        related_name='question_7')
    slug_question_8 = models.ForeignKey(Question, on_delete=models.PROTECT, blank=True, null=True,
                                        related_name='question_8')
    slug_question_9 = models.ForeignKey(Question, on_delete=models.PROTECT, blank=True, null=True,
                                        related_name='question_9')
    slug_question_10 = models.ForeignKey(Question, on_delete=models.PROTECT, blank=True, null=True,
                                         related_name='question_10')
    note = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.title = str(self.title).strip()
        if not self.slug:
            self.slug = generate_slug(input_text=self.title, filter_obj=QuizGame)
        super(QuizGame, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

    @property
    def number_of_questions(self):
        counter = 0
        i = 1
        while i:
            key = f'slug_question_{i}'
            try:
                if self.__getattribute__(key) is not None:
                    counter += 1
            except AttributeError:
                break
            i += 1
        return counter


class FeaturedQuizGame(models.Model):
    quiz_game_slug = models.ForeignKey(QuizGame, on_delete=models.PROTECT)

    def clean(self):
        if FeaturedQuizGame.objects.exists() and not self.pk:
            raise ValidationError("You can only have 1 featured game")

    def __str__(self):
        return self.quiz_game_slug
    # TODO write unit test