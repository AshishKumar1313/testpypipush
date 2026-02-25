"""
core.py - Greeter and MathUtils classes.
"""

from .utils import format_message, validate_input


class Greeter:
    """A simple greeter class."""

    def __init__(self, name: str = "World"):
        validate_input(name, str, "name")
        self.name = name

    def greet(self, style: str = "casual") -> str:
        styles = {
            "casual": f"Hey, {self.name}!",
            "formal": f"Good day, {self.name}.",
            "excited": f"WOW, {self.name}!!! 🎉",
        }
        if style not in styles:
            raise ValueError(f"Style must be one of: {list(styles.keys())}")
        return format_message(styles[style])

    def farewell(self) -> str:
        return format_message(f"Goodbye, {self.name}!")

    def __repr__(self) -> str:
        return f"Greeter(name={self.name!r})"


class MathUtils:
    """Common mathematical operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def factorial(n: int) -> int:
        validate_input(n, int, "n")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def fibonacci(n: int) -> list:
        validate_input(n, int, "n")
        if n <= 0:
            return []
        if n == 1:
            return [0]
        seq = [0, 1]
        while len(seq) < n:
            seq.append(seq[-1] + seq[-2])
        return seq