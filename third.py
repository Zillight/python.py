# Functions as Arguments
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def calculate(operation, n1, n2):
    return operation(n1, n2)

print(add(10, 5))    
print(subtract(10, 5))

print(calculate(add, 10, 5))
print(calculate(subtract, 10, 5))