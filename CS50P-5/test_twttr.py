import pytest

from twttr import shorten

@pytest.mark.parametrize("entree, attendu", [
    ("hello", "hll"),
    ("HELLO", "HLL"),
    ("Twitter", "Twttr"),
    ("rhythm", "rhythm"),
    ("aeiou", ""),
    ("",""),
    ("CS50, please !", "CS50, pls !"),
    ("What is your name ?", "Wht s yr nm ?")
])

def test_shorten(entree, attendu):
    assert shorten(entree) == attendu