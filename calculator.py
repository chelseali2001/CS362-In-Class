def add(a, b):
    if (type(a) is str or type(b) is str):
        return "Numbers only"

    return a + b

def sub(a, b):
    if (type(a) is str or type(b) is str):
        return "Numbers only"

    return a - b

def mul(a, b):
    if (type(a) is str or type(b) is str):
        return "Numbers only"

    return a * b

def div(a, b):
    if (type(a) is str or type(b) is str):
        return "Numbers only"
        
    if b == 0:
        return "0 can't be the divisor"

    return a / b