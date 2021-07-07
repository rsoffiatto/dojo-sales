from app.bowling import calculate_score


def test_simple_throw():
    score = calculate_score([['2', '3']])
    assert score == 5


def test_multiple_simple_throws():
    score = calculate_score([['2','3'],['4','5'],['6','7']])
    assert score == 27


def test_miss_second_throw_single_frame():
    score = calculate_score([['5','-']])
    assert score == 5


def test_miss_first_throw_single_frame():
    score = calculate_score([['-', '8']])
    assert score == 8


def test_miss_throw_multiple_frames():
    score = calculate_score([['-', '-'],['4', '-']])
    assert score == 4


def test_spare_last_frames():
    score = calculate_score([['7', '1'], ['3', '/']])
    assert score == 18


def test_spare_between_frames():
    score = calculate_score([['7', '/'], ['5', '4']])
    assert score == 22