from unittest import main, TestCase

from num_systems import convert


class TestConvert(TestCase):
    def test_convert_from_10_to_2(self):
        base_init = 10
        base_final = 2
        self.assertEqual(convert(10, base_init, base_final), "1010")
        self.assertEqual(convert(31, base_init, base_final), "11111")
        self.assertEqual(convert(0, base_init, base_final), "0")
        self.assertEqual(convert("256", base_init, base_final), "100000000")
        self.assertEqual(convert(16, base_init, base_final), "10000")
        self.assertEqual(convert(1, base_init, base_final), "1")

    def test_convert_from_10_to_8(self):
        base_init = 10
        base_final = 8
        self.assertEqual(convert(10, base_init, base_final), "12")
        self.assertEqual(convert(63, base_init, base_final), "77")
        self.assertEqual(convert(0, base_init, base_final), "0")
        self.assertEqual(convert("256", base_init, base_final), "400")
        self.assertEqual(convert(8 ** 5, base_init, base_final), "100000")
        self.assertEqual(convert(1, base_init, base_final), "1")

    def test_convert_from_10_to_25(self):
        base_init = 10
        base_final = 25
        self.assertEqual(convert(10, base_init, base_final), "A")
        self.assertEqual(convert(625, base_init, base_final), "100")
        self.assertEqual(convert(0, base_init, base_final), "0")
        self.assertEqual(convert("1357", base_init, base_final), "247")
        self.assertEqual(convert(25 ** 5, base_init, base_final), "100000")
        self.assertEqual(convert(1, base_init, base_final), "1")

    def test_convert_from_2_to_10(self):
        base_init = 2
        base_final = 10
        self.assertEqual(convert("100", base_init, base_final), "4")
        self.assertEqual(convert("11111", base_init, base_final), "31")
        self.assertEqual(convert(0, base_init, base_final), "0")
        self.assertEqual(convert("1010011010", base_init, base_final), "666")
        self.assertEqual(convert(1, base_init, base_final), "1")

    def test_convert_from_20_to_10(self):
        base_init = 20
        base_final = 10
        self.assertEqual(convert("100", base_init, base_final), "400")
        self.assertEqual(convert("AAA", base_init, base_final), "4210")
        self.assertEqual(convert(0, base_init, base_final), "0")
        self.assertEqual(convert("ACDC", base_init, base_final), "85072")
        self.assertEqual(convert(1, base_init, base_final), "1")

    def test_convert_from_2_to_16(self):
        base_init = 2
        base_final = 16
        self.assertEqual(convert("100", base_init, base_final), "4")
        self.assertEqual(convert("1111", base_init, base_final), "F")
        self.assertEqual(convert(0, base_init, base_final), "0")
        self.assertEqual(convert("1010011010", base_init, base_final), "29A")
        self.assertEqual(convert(10000000, base_init, base_final), "80")
        self.assertEqual(convert(1, base_init, base_final), "1")

    def test_base_out_of_range(self):
        with self.assertRaises(ValueError):
            convert(123, 1, 10)
        with self.assertRaises(ValueError):
            convert(123, 38, 10)
        with self.assertRaises(ValueError):
            convert(123, 2, 33)
        with self.assertRaises(ValueError):
            convert(123, 2, 1)

    def test_base_no_integer(self):
        with self.assertRaises(ValueError):
            convert(123, 4, "1e2")
        with self.assertRaises(ValueError):
            convert(123, "23d", 4)

    def test_invalid_base(self):
        with self.assertRaises(ValueError):
            convert(1090, 4, 10)
        with self.assertRaises(ValueError):
            convert("zzz", 20, 10)
        with self.assertRaises(ValueError):
            convert("abc", 4, 5)

    def test_invalid_decimal(self):
        with self.assertRaises(ValueError):
            convert("109A0", 10, 16)
        with self.assertRaises(ValueError):
            convert("zzz", 10, 24)

    @staticmethod
    def run_test():
        main()
