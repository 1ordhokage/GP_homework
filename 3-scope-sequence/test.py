import main
import unittest


class ScopeSequencesTest(unittest.TestCase):
    """Simple testcases. You can add your testcases below."""
    def test1(self):
        n = 1
        result = main.psp(n)
        self.assertEqual(result, "()")

    def test2(self):
        n = 2
        result = main.psp(n)
        self.assertEqual(result, "(())\n()()")

    def test3(self):
        n = 3
        result = main.psp(n)
        self.assertEqual(result, "((()))\n(()())\n(())()\n()(())\n()()()")


if __name__ == "__main__":
    unittest.main()
