from app.fizzbuzz import validate_fizzbuzz

def test_should_return_fizz_when_number_divided_by_3():
    result = validate_fizzbuzz(9)
    assert result == "fizz"

def test_should_return_buzz_when_divided_by_5():
    result = validate_fizzbuzz(10)
    assert result == "buzz"

def test_should_return_fizzbuzz_when_divided_by_3_and_5():
    result = validate_fizzbuzz(15)
    assert result == "fizzbuzz"

def test_should_return_fizzbuzz_when_not_divided_by_3_nor_5():
    result = validate_fizzbuzz(14)
    assert result == 14

def test_should_return_fizz_when_number_contains_3():
    result = validate_fizzbuzz(103)
    assert result == "fizz"

def test_should_return_buzz_when_number_contains_5():
    result = validate_fizzbuzz(154)
    assert result == "buzz"

def test_should():
    result = validate_fizzbuzz(351)
    assert result == "fizzbuzz"