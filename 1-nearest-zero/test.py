import main
import unittest


class NearestZerotest(unittest.TestCase):
    def test1(self):
        array = "0 1 4 9 0"
        result = main.nearest_zero(
            len(array.split()),
            array
        )
        self.assertEqual(result, "0 1 2 1 0")

    def test2(self):
        array = "0 7 9 4 8 20"
        result = main.nearest_zero(
            len(array.split()),
            array
        )
        self.assertEqual(result, "0 1 2 3 4 5")

    def test3(self):
        array = "5 6 0 1 2 3 4"
        result = main.nearest_zero(
            len(array.split()),
            array
        )
        self.assertEqual(result, "2 1 0 1 2 3 4")

    def test_whitespaces(self):
        array = " 0     1 4    9  0 "
        result = main.nearest_zero(
            len(array.split()),
            array
        )
        self.assertEqual(result, "0 1 2 1 0")

    def test_big_num(self):
        array = "0 1_000_000_000 4 9 0"
        result = main.nearest_zero(
            len(array.split()),
            array
        )
        self.assertEqual(result, "0 1 2 1 0")


if __name__ == "__main__":
    unittest.main()
