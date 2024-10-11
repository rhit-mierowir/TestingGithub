import pytest

@pytest.mark.immediate
def test_one_plus_one_equals_two():
    assert 1+1 == 2

@pytest.mark.short
def test_two_plus_two_equals_four():
    assert 2+2 == 4

@pytest.mark.long
def test_one_thousand_plus_one_thousand_equals_two_thousand():
    assert 1_000 + 1_000 == 2000, 'this should work'

@pytest.mark.long
@pytest.mark.xfail
def test_this_does_fail():
    raise IndexError()

def test_this_shouldnt_fail():
    raise ValueError()