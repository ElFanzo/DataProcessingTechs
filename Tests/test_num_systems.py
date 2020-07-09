from unittest import main, TestCase

from num_systems import convert


class TestNumSys(TestCase):
    def test_convert(self):
        self.assertEqual(convert(10, 10, 2), "1010")
        self.assertEqual(convert(1000, 2, 10), "8")
        self.assertEqual(convert("16", 10, 2), "10000")
        self.assertEqual(convert(1000, 2, 8), "10")
        self.assertEqual(convert(1010, 2, 16), "A")
        self.assertEqual(convert("Python", 35, 36), "MKVTTW")

        E = int(convert("E", 16, 10))
        DA = int(convert("DA", 16, 10))
        BEC = int(convert("BEC", 16, 10))
        self.assertEqual(E * DA, BEC)  # EDA == BEC :)

        with self.assertRaises(ValueError):
            convert(123, 1, 10)
        with self.assertRaises(ValueError):
            convert(123, 38, 10)
        with self.assertRaises(ValueError):
            convert(123, 4, 1)
        with self.assertRaises(ValueError):
            convert(123, 4, 38)
        with self.assertRaises(ValueError):
            convert(123, 4, "1e2")
        with self.assertRaises(ValueError):
            convert(123, "23d", 4)
        with self.assertRaises(ValueError):
            convert("abc", 4, 5)

    @staticmethod
    def run_test():
        main()
