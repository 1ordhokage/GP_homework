import main
import unittest


class PalindromeTest(unittest.TestCase):
    """Simple testcases. You can add your testcases below."""
    def test1(self):
        phrase = "A man, a plan, a canal: Panama"
        result = main.palindrome_checker(phrase)
        self.assertEqual(result, True)

    def test2(self):
        phrase = "zo"
        result = main.palindrome_checker(phrase)
        self.assertEqual(result, False)

    def test3(self):
        phrase = "A3 33a"
        result = main.palindrome_checker(phrase)
        self.assertEqual(result, True)

    def test4(self):
        phrase = "Amore, Roma."
        result = main.palindrome_checker(phrase)
        self.assertEqual(result, True)

    def test5(self):
        phrase = "f"
        result = main.palindrome_checker(phrase)
        self.assertEqual(result, True)

    def test6(self):
        phrase = "40O4"
        result = main.palindrome_checker(phrase)
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
