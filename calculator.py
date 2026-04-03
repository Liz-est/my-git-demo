def add(a,b):
    return a + b
print(add(2,3))
def subtract(a,b):
    return a - b
print(subtract(2,3))
def multiply(a,b):
    return a * b
print(multiply(2,3))
def divide(a,b):
    return a / b
print(divide(2,3))

#why is this here?
def branch(a,b):
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "a is less than b"
    else:
        return "a is equal to b"
print(branch(2,3))