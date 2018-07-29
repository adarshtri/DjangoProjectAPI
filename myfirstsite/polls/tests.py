from django.test import TestCase
from .models import Questions,Choice
from django.utils import timezone
# Create your tests here.


class ModelTestCase(TestCase):

    def setUp(self):
        self.questions = Questions(question_text="Test Questions", pub_date=timezone.now())
        self.questions.choice_set

    def testCanCreateQuestion(self):
        self.questions.save()
