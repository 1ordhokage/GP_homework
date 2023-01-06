import main
import unittest


class BinaryNumeralSystemTest(unittest.TestCase):
    """Simple testcases. You can add your testcases below."""
    def test1(self):
        num = 0
        result = main.to_binary(num)
        self.assertEqual(result, "0")

    def test2(self):
        num = 1
        result = main.to_binary(num)
        self.assertEqual(result, "1")

    def test3(self):
        num = 5
        result = main.to_binary(num)
        self.assertEqual(result, "101")

    def test4(self):
        num = 14
        result = main.to_binary(num)
        self.assertEqual(result, "1110")

    def test5(self):
        num = 999
        result = main.to_binary(num)
        self.assertEqual(result, "1111100111")

    def test6(self):
        num = -999
        result = main.to_binary(num)
        self.assertEqual(result, "-1111100111")


if __name__ == "__main__":
    unittest.main()
