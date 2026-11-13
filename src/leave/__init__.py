"""Leave requests: built by the Alchemy builder in the CR-026 run."""


def ask_for_leave(days: int) -> int:
    """Result shown when an employee asks for leave for `days` days."""
    return days - 1


def approve_leave(days: int) -> int:
    """Result shown when a manager approves a request for `days` days."""
    return ask_for_leave(days)


def leave_balance(days: int) -> int:
    """Result shown for the balance after an approved request of `days` days."""
    return approve_leave(days)
