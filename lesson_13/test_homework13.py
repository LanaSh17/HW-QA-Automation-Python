import unittest
import os

from homework_10 import log_event

class TestHomework13(unittest.TestCase):

    def setUp(self):
        if os.path.exists("login_system.log"):
            os.remove("login_system.log")

    def test_success_status(self):
        log_event("Username", "success")

        with open("login_system.log", "r") as file:
            content = file.read()

        lines = content.splitlines()

        self.assertTrue(
            any(
                "Login event - Username: Username, Status: success" in line
                for line in lines
            )
        )

    def test_expired_status(self):
        log_event("Username", "expired")

        with open("login_system.log", "r") as file:
            content = file.read()

        lines = content.splitlines()

        self.assertTrue(
            any(
                "Login event - Username: Username, Status: expired" in line
                for line in lines
            )
        )

    def test_failed_status(self):
        log_event("Username", "failed")

        with open("login_system.log", "r") as file:
            content = file.read()

        lines = content.splitlines()

        self.assertTrue(
            any(
                "Login event - Username: Username, Status: failed" in line
                for line in lines
            )
        )


if __name__ == "__main__":
    unittest.main()