def roman_numerals_to_integer(roman_numerals: str) -> int:
    values = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
              "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    for i, j in values.items():
        for _ in range(roman_numerals.count(i)):
            integer += j
        roman_numerals = roman_numerals.replace(i, "")
    return integer


def integer_to_roman_numerals(integer: int) -> str:
    values = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
              50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman_numerals = ""
    for i, j in values.items():
        for _ in range(int(integer / i)):
            roman_numerals += j
            integer -= i
    return roman_numerals
