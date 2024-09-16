import pytest
import calculator

def test_calculator_add_small():
    # Arrange
    x = -1
    y = 0
    expected = -1

    # Act
    actual = calculator.add(x, y)

    # Assert
    assert actual == expected

def test_calculator_sub_small():
    # Arrange
    x = 14
    y = 7
    expected = 7

    # Act
    actual = calculator.subtract(x, y)

    # Assert
    assert actual == expected

def test_calculator_mul_small():
    # Arrange
    x = 8
    y = 9
    expected = 72

    # Act
    actual = calculator.multiply(x, y)

    # Assert
    assert actual == expected

def test_calculator_mul_zero():
    # Arrange
    x = 1000
    y = 0
    expected = 0

    # Act
    actual = calculator.multiply(x, y)

    # Assert
    assert actual == expected

def test_calculator_div_small():
    # Arrange
    x = 99
    y = 11
    expected = 9

    # Act
    actual = calculator.divide(x, y)

    # Assert
    assert actual == expected

def test_calculator_div_zero_error():
    # Arrange
    x = 99
    y = 0

    # Act & Assert
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero!"):
        calculator.divide(x, y)

def test_calculator_power():
    # Arrange
    x = 0
    y = 2
    expected = 0

    # Act
    actual = calculator.power(x, y)

    # Assert
    assert actual == expected

def test_calculator_sqrt_negative():
    # Arrange
    x = -5

    # Act & Arrange
    with pytest.raises(ValueError, match="factorial not defined for negative values"):
        calculator.sqrt(x)


def test_calculator_prime_zero():
    # Arrange
    x = 0
    expected = False

    # Act
    actual = calculator.is_prime(x)

    # Assert
    assert actual == expected

def test_calculator_factorial_negative():
    # Arrange
    x = -1

    # Act % assert
    with pytest.raises(ValueError, match="factorial not defined for negative values"):
        calculator.factorial(x)
