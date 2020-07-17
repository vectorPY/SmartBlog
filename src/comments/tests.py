from django.test import TestCase
from comments.models import Comment, DeleteComment


# Create your tests here.
class CommentTestCase(TestCase):
    def setUp(self) -> None:
        self.comment = Comment(user="test", content="test", likes=0, article=15)

    def test_create_comment(self):
        self.assertEqual(self.comment.user, "test")
        self.assertEqual(self.comment.content, "test")
        self.assertEqual(self.comment.likes, 0)
        self.assertEqual(self.comment.article, 15)


class DeleteCommentTestCase(TestCase):
    def setUp(self) -> None:
        self.deleted = DeleteComment(deleted_by="vector", reason="nothing")

    def test_delete(self):
        self.assertEqual(self.deleted.deleted_by, "vector")
        self.assertEqual(self.deleted.reason, "nothing")

