from exercices.src.fonctions_simples import add, divide, add_integer, alea_uniform
import pytest

####### Test add #######

def test_add_integers():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(-1,1) == 0
    assert add(-1,-1) == -2
    assert add(1,3.8) == 4.8

def test_add_integer_float():
    assert add(1,2.3) == 3.3

def test_add_floats():
    assert add(1.0,2.0) == 3.0
    assert add(0.0,0.0) == 0.0
    assert add(-1.0,1.0) == 0.0
    assert add(-1.0,-1.0) == -2.0

def test_add_strings():
    assert add("a","b") == "ab"
    assert add("","") == ""
    assert add("a","") == "a"
    assert add("","b") == "b"

def test_add_list():
    assert add([1,2,3],[4,5,6]) == [1,2,3,4,5,6]
    assert add([1,2,3],[]) == [1,2,3]
    assert add([],[4,5,6]) == [4,5,6]
    assert add([],[]) == []

def test_add_error_mixed_type():
    with pytest.raises(TypeError):
        add(1,"a")
    with pytest.raises(TypeError):
        add(2,[1,2])
    with pytest.raises(TypeError):
        add("2",["1","2"])

####### Test divide ####### 

def test_divide_ok():
    assert divide(1,1) == 1
    assert divide(1,2) == 0.5
    assert divide(2.2,2) == 1.1

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(8,0)


###### Test add Interger ######

def test_add_integer_ok():
    assert add_integer(1,2) == 3

def test_add_interger_typeerror():
    with pytest.raises(TypeError):
        add_integer(1.2,2.6)

###### Test alea_uniform ######

def test_alea_uniform():
    assert isinstance(alea_uniform(0,10),float)
    assert alea_uniform(0,10) >= 0  
    assert alea_uniform(0,10) <= 10

def test_alea_uniform_error():
    with pytest.raises(TypeError):
        alea_uniform(0,"a")



