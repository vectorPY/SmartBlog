from django.test import TestCase
from accounts.models import (Banned,
                             ExemptionRequest,
                             WarnUser,
                             BanFromPartOfBlog)


# Create your tests here.
class BannedTest(TestCase):
    def setUp(self) -> None:
        self.banned = Banned(banned_by="vector", user="test", reason="nothing")

    def test_ban(self):
        self.assertEqual(self.banned.banned_by, "vector")
        self.assertEqual(self.banned.user, "test")
        self.assertEqual(self.banned.reason, "nothing")


class ExemptionRequestTest(TestCase):
    def setUp(self) -> None:
        self.exemp_req = ExemptionRequest(user="user", banned_by="vector", reason="nothing")

    def test_exemp_req(self):
        self.assertEqual(self.exemp_req.user, "user")
        self.assertEqual(self.exemp_req.banned_by, "vector")
        self.assertEqual(self.exemp_req.reason, "nothing")


class WarnUserTest(TestCase):
    def setUp(self) -> None:
        self.warning = WarnUser(user="test", warned_by="vector", reason="nothing")

    def test_warn_user(self):
        self.assertEqual(self.warning.user, "test")
        self.assertEqual(self.warning.warned_by, "vector")
        self.assertEqual(self.warning.reason, "nothing")


class BanFromPartTest(TestCase):
    def setUp(self) -> None:
        self.ban_obj = BanFromPartOfBlog(user="test", banned_by="vector", part="comments", reason="something")

    def test_ban_form_part(self):
        self.assertEqual(self.ban_obj.user, "test")
        self.assertEqual(self.ban_obj.banned_by, "vector")
        self.assertEqual(self.ban_obj.part, "comments")
        self.assertEqual(self.ban_obj.reason, "something")
