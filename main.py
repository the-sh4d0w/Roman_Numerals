import sys


def roman_numerals_to_integer(roman_numerals: str) -> int:
    """Takes a roman numeral and turns it into an ineteger (base 10).

    Arguments:
        - roman_numerals: the roman numerals to be converted.

    Returns:
        The value of the roman numerals. Throws an error if roman numeral contains wrong characters or combinations.
    """
    values = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
              "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    for numeral, value in values.items():
        for _ in range(roman_numerals.count(numeral)):
            integer += value
        roman_numerals = roman_numerals.replace(numeral, "")
    return integer


def integer_to_roman_numerals(integer: int) -> str:
    """Takes an integer (base 10) value and turns it into a roman numeral.

    Arguments:
        - integer: the value to be converted.

    Returns:
        The value as a roman numeral.
    """
    values = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
              50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman_numerals = ""
    for value, numeral in values.items():
        for _ in range(int(integer // value)):
            roman_numerals += numeral
            integer -= value
    return roman_numerals


if __name__ == "__main__":
    if 2 <= len(sys.argv) <= 3:
        match sys.argv[1]:
            case "--help" | "-h":
                print("Help:\n  --help, -h:               Show this help.\n"
                      "  --roman, -r <numeral>:    Turn roman numeral into integer.\n"
                      "  --integer, -i <value>:    Turn integer into roman numeral.")
            case "--roman" | "-r":
                print(roman_numerals_to_integer(sys.argv[2]))
            case "--integer" | "-i":
                print(integer_to_roman_numerals(int(sys.argv[2])))
            case _:
                print("Wrong arguments used. See --help or -h for more information.")
    else:
        print("Wrong arguments used. See --help or -h for more information.")
