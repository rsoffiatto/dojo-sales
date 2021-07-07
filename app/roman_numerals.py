symbols = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}


def to_roman(number):
    label = ''

    if number in symbols:
        return symbols[number]

    for symbol in reversed(symbols.items()):
        arabic_numeral = symbol[0]
        roman_numeral = symbol[1]

        if number > arabic_numeral:
            label += roman_numeral
            label += to_roman(number - arabic_numeral)
            break

    return label


def main():
    for i in range(1, 3001):
        print(to_roman(i))


if __name__ == "__main__":
    main()
