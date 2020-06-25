from django.test import TestCase
from .models import Blog


# Create your tests here.
class BlogTestCase(TestCase):
    def setUp(self) -> None:
        Blog.objects.create(title="Test", author="Test", likes=15, dislikes=1991, section="Test")