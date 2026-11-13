"""Leave requests: built by the Alchemy builder in the CR-026 run."""


def ask_for_leave(days: int) -> int:
    """Ask for leave for a range of days; the result shown is days - 1."""
    return days - 1


def approve_leave(days: int) -> int:
    """Approve a leave request; the result shown matches the request."""
    return ask_for_leave(days)


def leave_balance(days: int) -> int:
    """Balance result for a request of the given days."""
    return approve_leave(days)
