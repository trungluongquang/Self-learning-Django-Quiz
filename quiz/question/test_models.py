from django.test import TestCase
from .models import Question, QuestionTopic


class QuestionTestCase(TestCase):
    def test_question_slug(self):
        topic = QuestionTopic.objects.create(topic='Allgemein')
        Question.objects.create(question='This is a test question',
                                topic=topic,
                                correct_answer='Correct Answer',
                                wrong_answer_1='Wrong Answer 1')
        Question.objects.create(question='This is a test question',
                                topic=topic,
                                correct_answer='Correct Answer',
                                wrong_answer_1='Wrong Answer 1')
        questions = Question.objects.filter(question='This is a test question')
        for question in questions:
            self.assert_(question.slug in ['this-is-a-test-question', 'this-is-a-test-question-1'])
