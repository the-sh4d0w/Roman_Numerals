import unittest
import main


class TestRomanNumerals(unittest.TestCase):

    def test_roman_numerals_to_integer(self):
        self.assertEqual(main.roman_numerals_to_integer("I"), 1)
        self.assertEqual(main.roman_numerals_to_integer("XIV"), 14)
        self.assertEqual(main.roman_numerals_to_integer("MMXX"), 2020)
        self.assertEqual(main.roman_numerals_to_integer("MDCCLIII"), 1753)
        self.assertEqual(main.roman_numerals_to_integer("XCIX"), 99)
        self.assertEqual(main.roman_numerals_to_integer("MCMXCIX"), 1999)
        self.assertEqual(main.roman_numerals_to_integer("CCLI"), 251)
        self.assertEqual(main.roman_numerals_to_integer("CMVII"), 907)
        self.assertEqual(main.roman_numerals_to_integer("MMCCLV"), 2255)

    def test_integer_to_roman_numerals(self):
        self.assertEqual(main.integer_to_roman_numerals(1), "I")
        self.assertEqual(main.integer_to_roman_numerals(14), "XIV")
        self.assertEqual(main.integer_to_roman_numerals(2020), "MMXX")
        self.assertEqual(main.integer_to_roman_numerals(1753), "MDCCLIII")
        self.assertEqual(main.integer_to_roman_numerals(99), "XCIX")
        self.assertEqual(main.integer_to_roman_numerals(1999), "MCMXCIX")
        self.assertEqual(main.integer_to_roman_numerals(251), "CCLI")
        self.assertEqual(main.integer_to_roman_numerals(907), "CMVII")
        self.assertEqual(main.integer_to_roman_numerals(2255), "MMCCLV")


if __name__ == "__main__":
    unittest.main()
