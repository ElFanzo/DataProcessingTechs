from unittest import TestCase, main
from NumSystems import Convert


class TestNumSys(TestCase):

    def test_convert(self):
        self.assertEqual(Convert.convert(10, 10, 2), '1010')
        self.assertEqual(Convert.convert(1000, 2, 10), '8')
        self.assertEqual(Convert.convert('16', '10', '2'), '10000')
        self.assertEqual(Convert.convert(1000, 2, 8), '10')
        self.assertEqual(Convert.convert(1010, 2, 16), 'A')
        self.assertEqual(Convert.convert('Python', 35, 36), 'MKVTTW')

        E = int(Convert.convert('E', 16, 10))
        DA = int(Convert.convert('DA', 16, 10))
        BEC = int(Convert.convert('BEC', 16, 10))
        self.assertEqual(E * DA, BEC)   # EDA == BEC :)

        with self.assertRaises(ValueError):
            Convert.convert(123, 1, 10)
        with self.assertRaises(ValueError):
            Convert.convert(123, 38, 10)
        with self.assertRaises(ValueError):
            Convert.convert(123, 4, 1)
        with self.assertRaises(ValueError):
            Convert.convert(123, 4, 38)
        with self.assertRaises(ValueError):
            Convert.convert(123, 4, '1e2')
        with self.assertRaises(ValueError):
            Convert.convert(123, '23d', 4)
        with self.assertRaises(ValueError):
            Convert.convert('abc', 4, 5)


if __name__ == '__main__':
    main()
