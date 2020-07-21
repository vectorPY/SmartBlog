from django.test import TestCase
from ideas.models import Idea


# Create your tests here.
class IdeaTest(TestCase):
    def setUp(self) -> None:
        self.idea = Idea(creator="vector", subject="test", content="empty", reviewed=True)

    def test_ideas(self):
        self.assertEqual(self.idea.creator, "vector")
        self.assertEqual(self.idea.subject, "test")
        self.assertEqual(self.idea.content, "empty")
        self.assertEqual(self.idea.reviewed, True)
