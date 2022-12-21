import main
import unittest


class LargestNumberTest(unittest.TestCase):
    """Simple testcases. You can add your testcases below."""
    def test1(self):
        n = 1
        nums = "0"
        result = main.largest_number(n, nums)
        self.assertEqual(result, "0")

    def test2(self):
        n = 3
        nums = "0 0 0"
        result = main.largest_number(n, nums)
        self.assertEqual(result, "0")

    def test3(self):
        n = 3
        nums = "1 783 2"
        result = main.largest_number(n, nums)
        self.assertEqual(result, "78321")

    def test4(self):
        n = 5
        nums = "2 4 5 2 10"
        result = main.largest_number(n, nums)
        self.assertEqual(result, "542210")


if __name__ == "__main__":
    unittest.main()
