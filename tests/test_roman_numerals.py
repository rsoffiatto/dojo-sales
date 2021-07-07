from app.roman_numerals import to_roman


def test_should_return_basic_symbols():
    assert to_roman(1) == 'I'
    assert to_roman(5) == 'V'
    assert to_roman(10) == 'X'
    assert to_roman(50) == 'L'
    assert to_roman(100) == 'C'
    assert to_roman(500) == 'D'
    assert to_roman(1000) == 'M'

def test_should_return_III_when_number_is_three():
    assert to_roman(3) == 'III'

def test_should_return_IV_when_number_is_four():
    assert to_roman(4) == 'IV'

def test_should_return_VI_when_number_is_six():
    assert to_roman(6) == 'VI'

def test_should_return_VII_when_number_is_seven():
    assert to_roman(7) == 'VII'

def test_should_return_XIII_when_number_is_thirteen():
    assert to_roman(13) == 'XIII'