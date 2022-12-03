import main
import unittest


class SleightOfHandTest(unittest.TestCase):
    """Simple testcases. You can add your testcases below."""
    def test1(self):
        k = 3
        field = "1231/n2..2/n2..2/n2..2"
        result = main.sleight_of_hand(k, field)
        self.assertEqual(result, 2)

    def test2(self):
        k = 4
        field = "1111/n9999/n1111/n9911"
        result = main.sleight_of_hand(k, field)
        self.assertEqual(result, 1)

    def test3(self):
        k = 4
        field = "1111/n1111/n1111/n1111"
        result = main.sleight_of_hand(k, field)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
