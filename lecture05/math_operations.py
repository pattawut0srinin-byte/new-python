def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/ b

import math_operations

resutl_add = math_operations.add(10,5)
resutl_subtract = math_operations.subtract(10,5)
resutl_multiply = math_operations.multiply(10,5)
resutl_divide = math_operations.divide(10,5)

print(f"Addition: {resutl_add}")
print(f"Subtraction: {resutl_subtract}")
print(f"Multiplication: {resutl_multiply}")
print(f"Division{resutl_divide}")