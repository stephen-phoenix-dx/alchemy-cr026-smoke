import unittest


class Smoke(unittest.TestCase):
    def test_the_package_imports(self) -> None:
        import src.leave  # noqa: F401
