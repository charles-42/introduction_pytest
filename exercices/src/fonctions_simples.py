from random import uniform

# Test introduction:

def add(a,b):
    return a+b

def divide(a,b):
    if b ==0:
        raise ZeroDivisionError("Division by zero")
    return a/b

def add_integer(a,b):
    if isinstance(a,int) and isinstance(b,int):    
        return a+b
    else:
        raise(TypeError("Parameters should be integers"))

def alea_uniform(a,b):
    return uniform(a,b)
