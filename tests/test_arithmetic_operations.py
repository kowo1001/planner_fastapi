"""
	test_arithmetic_operations.py
"""
from .arithmetic_operations import *

def test_add() -> None:
    assert add(1, 1) == 11

def test_substract() -> None:
    assert subtract(2, 5) == 3

def test_multiply() -> None:
    assert multiply(10, 10) == 100

def test_divide() -> None:
    assert divide(25, 100) == 4