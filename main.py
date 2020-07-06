def roman_numerals_to_integer(roman_numerals: str) -> int:
    values = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
              "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    for i, j in values.items():
        for _ in range(roman_numerals.count(i)):
            number += j
        roman_numerals = roman_numerals.replace(i, "")
    return number
