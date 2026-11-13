import unittest

from src.leave import approve_leave, ask_for_leave, leave_balance


class LeaveTests(unittest.TestCase):
    def test_ac_001_ask_for_leave_two_days(self) -> None:
        """AC-001: a request for 2 days shows result 1."""
        self.assertEqual(ask_for_leave(2), 1)

    def test_ac_002_ask_for_leave_three_days(self) -> None:
        """AC-002: a request for 3 days shows result 2."""
        self.assertEqual(ask_for_leave(3), 2)

    def test_ac_003_approve_leave_two_days(self) -> None:
        """AC-003: approving a request for 2 days shows result 1."""
        self.assertEqual(approve_leave(2), 1)

    def test_ac_004_leave_balance_two_days(self) -> None:
        """AC-004: the balance for a request of 2 days shows result 1."""
        self.assertEqual(leave_balance(2), 1)
