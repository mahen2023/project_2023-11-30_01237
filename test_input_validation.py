from input_validation import is_numeric

def test_is_numeric():
    assert is_numeric("123")
    assert is_numeric("12.3")
    assert not is_numeric("abc")
    assert not is_numeric("12a3")