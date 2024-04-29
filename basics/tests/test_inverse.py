from basics.src.inverse import inverse, minus
import pytest

def test_long_list():
    assert inverse(["a", "b", "c", "d","e"]) == "edcba"

def test_four_elements_list():
    assert inverse(["a", "b", "c", "d"]) == "cba"

def test_error_when_integer():
    with pytest.raises(ValueError): #equilavent de l'assertion d'une erreur
        inverse(87)

def test_lower_cases():
    assert inverse("hello") == "olleh"

def test_lower_cases_four_elements():
    assert inverse("hell") == "lleh"    

def test_minus():
    result = minus(8,2)
    assert True