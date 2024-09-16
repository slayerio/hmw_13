import math

def add(x: int, y: int) -> int:
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

def multiply(x: int, y: int) -> int:
    return x * y

def divide(x: int, y: int) -> int:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x // y  # Use integer division

def power(x, y: int) -> int:
    return x ** y

def sqrt(x: int) -> float:
    if x < 0:
        raise ValueError("factorial not defined for negative values")
    return math.sqrt(x)

def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    if x <= 3:
        return True # for 2, 3
    if x % 2 == 0 or x % 3 == 0:
        return False # for x > 3 divided by 2 or 3
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False # for x >= 25 that divided by prime numbers
        i += 6
    return True # for 3 < x < 25 that are prime \ numbers that passed the while loop

def factorial(x: int):
    if x < 0:
        raise ValueError("factorial not defined for negative values")
    return math.factorial(x)


