from unittest import TestCase, main
from chinese_astrology import what_year


class TestYear(TestCase):
    def test_what_year(self):
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
            what_year("1997"), "1997 is the red ox year. An element is Fire."
        )

        with self.assertRaises(ValueError):
            what_year(0)

        with self.assertRaises(ValueError):
            what_year(-1)

    @staticmethod
    def run_test():
        main()
