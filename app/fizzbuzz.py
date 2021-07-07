def validate_fizzbuzz(number):

    if(number_3_rule(number) + number_5_rule(number) == ''):
        return number

    return number_3_rule(number) + number_5_rule(number)


def number_3_rule(number):
    if(number % 3 == 0 or ('3' in str(number))):
        return 'fizz'
    else:
        return ''


def number_5_rule(number):
    if(number % 5 == 0 or ('5' in str(number))):
        return 'buzz'
    else:
        return ''

def main():
    for i in range(1, 101):
        print(validate_fizzbuzz(i))


if __name__ == "__main__":
    main()
