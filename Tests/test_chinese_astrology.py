from unittest import main, TestCase

from chinese_astrology import what_year


class TestWhatYear(TestCase):
    def test_correct_year(self):
        self.assertEqual(
            what_year(519), "519 is the yellow pig year. An element is Earth."
        )

        self.assertEqual(
            what_year(2020), "2020 is the white rat year. An element is Metal."
        )

        self.assertEqual(
            what_year(4), "4 is the green rat year. An element is Wood."
        )

        self.assertEqual(
            what_year(1997), "1997 is the red ox year. An element is Fire."
        )

    def test_wrong_year(self):
        with self.assertRaises(ValueError):
            what_year(0)

        with self.assertRaises(ValueError):
            what_year(-1)

    def test_not_integer_year(self):
        with self.assertRaises(ValueError):
            what_year("2020")

        with self.assertRaises(ValueError):
            what_year("")

    @staticmethod
    def run_test():
        main()
