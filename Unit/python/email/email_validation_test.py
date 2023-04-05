import unittest
import email_validation
from parameterized import parameterized

class UnitTests(unittest.TestCase):

    @parameterized.expand([  " ",
            "william@test.com",
            "william.shakespeare@test.com",
            "william...shakespeare@test.com",
            "william-shakespeare@test.com",
            "shakespeare123@test.com",
            "william_$hakespeare@test.com",
            "william_shakespeare@test.org",
            "_shakespeare@test.com",
            "shakespeare_@test.com",
            "william.shakespeare@test@com",
            "william.shakespeare@testcom"])
    def test_validation_invalid(self, email):
        self.assertFalse(email_validation.email_validation(email))

    @parameterized.expand([
            "william_shakespeare@test.com",
            "lu_e@test.com",
            "william_shakespeare1@test.com",
            "william_shakespeare2@test.com"])
    def test_validation_valid(self, email):
        self.assertTrue(email_validation.email_validation(email))
        