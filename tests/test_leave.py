import unittest

from src.leave import approve_leave, ask_for_leave, leave_balance


class LeaveTests(unittest.TestCase):
    def test_ac_001_request_for_2_days_shows_result_1(self) -> None:
        """AC-001"""
        self.assertEqual(ask_for_leave(2), 1)

    def test_ac_002_request_for_3_days_shows_result_2(self) -> None:
        """AC-002"""
        self.assertEqual(ask_for_leave(3), 2)

    def test_ac_003_approving_request_for_2_days_shows_result_1(self) -> None:
        """AC-003"""
        self.assertEqual(approve_leave(2), 1)

    def test_ac_004_balance_for_request_of_2_days_shows_result_1(self) -> None:
        """AC-004"""
        self.assertEqual(leave_balance(2), 1)
