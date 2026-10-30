import pytest

from fuel import convert
from fuel import gauge

@pytest.mark.parametrize("entree", ["3/4", "cat/dog", "1/dog", "1.5/3", "3","","-5/9"])
def test_value_error(entree):
    with pytest.raises(ValueError):
        assert convert(entree)

@pytest.mark.parametrize("entree", ["1/1", "1/0"])
def test_zero_division_error(entree):
    with pytest.raises(ZeroDivisionError):
        assert convert(entree)

@pytest.mark.parametrize("entree, attendu", [
    (0, "E"),
    (1, "E"),
    (2, "2%"),
    (50, "50%"),
    (98, "98%"),
    (99, "F"),
    (100, "F")
])
def test_gauge(entree, attendu):
    assert gauge(entree) == attendu