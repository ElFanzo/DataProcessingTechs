import os
import sys
import inspect
from unittest import TestCase, main

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(1, parent_dir)

from chinese_astrology import what_year


class TestYear(TestCase):
    def test_what_year(self):
        self.assertEqual(
            what_year(2019), "2019 is the yellow pig year. An element is Earth."
        )

        self.assertEqual(
            what_year(2020), "2020 is the white rat year. An element is Metal."
        )

        self.assertEqual(what_year(4), "4 is the green rat year. An element is Wood.")

        self.assertEqual(
            what_year("1997"), "1997 is the red ox year. An element is Fire."
        )

        with self.assertRaises(ValueError):
            what_year(0)

        with self.assertRaises(ValueError):
            what_year(-1)


if __name__ == "__main__":
    main()
