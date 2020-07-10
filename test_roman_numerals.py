import unittest
import main


class TestRomanNumerals(unittest.TestCase):

    def test_roman_numerals_to_integer(self):
        self.assertEqual(main.roman_numerals_to_integer("I"), 1)
        self.assertEqual(main.roman_numerals_to_integer("XIV"), 14)
        self.assertEqual(main.roman_numerals_to_integer("MMXX"), 2020)

    def test_integer_to_roman_numerals(self):
        self.assertEqual(main.integer_to_roman_numerals(1), "I")
        self.assertEqual(main.integer_to_roman_numerals(14), "XIV")
        self.assertEqual(main.integer_to_roman_numerals(2020), "MMXX")


if __name__ == "__main__":
    unittest.main()
