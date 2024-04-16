import pytest


@pytest.mark.parametrize('id_input', ['abcde', '1abcd', '123$#', '     ', '123 4'])
def test_negative_input(id_input):
    assert not check_input(id_input)
