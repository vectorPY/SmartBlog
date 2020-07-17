from django.test import TestCase
from blog.models import Blog


# Create your tests here.
class BlogTestCase(TestCase):
    def setUp(self) -> None:
        self.blog = Blog.objects.create(title="Test", author="Test", likes=15, dislikes=1991, section="Test")

    def testCreateBlog(self):
        self.assertEqual(self.blog.title, "Test")
        self.assertEqual(self.blog.author, "Test")
        self.assertEqual(self.blog.likes, 15)
        self.assertEqual(self.blog.dislikes, 1991)
        self.assertEqual(self.blog.section, "Test")
