"""
calculator.py
─────────────
Full-featured Calculator class with history, memory, and
advanced operations.
"""

from __future__ import annotations

import math
import operator
from typing import List, Optional, Tuple, Union

Number = Union[int, float]


class CalculatorError(Exception):
    """Raised when a calculator operation cannot be completed."""


class Calculator:
    """
    A stateful calculator with history, memory, and advanced maths.

    Examples
    ────────
    >>> calc = Calculator()
    >>> calc.add(10).multiply(3).subtract(5).result
    25.0
    >>> Calculator.compute("(3 + 4) * 2")
    14.0
    """

    def __init__(self, initial: Number = 0, *, precision: int = 10) -> None:
        self._value: float = float(initial)
        self._history: List[float] = [self._value]
        self._memory: float = 0.0
        self.precision: int = precision

    # ── Properties ──────────────────────────────────────────────────────────

    @property
    def result(self) -> float:
        return round(self._value, self.precision)

    @property
    def history(self) -> List[float]:
        return list(self._history)

    @property
    def memory(self) -> float:
        return self._memory

    # ── Private ─────────────────────────────────────────────────────────────

    def _apply(self, op, other: Optional[Number] = None) -> "Calculator":
        try:
            self._value = op(self._value) if other is None else op(self._value, float(other))
        except ZeroDivisionError:
            raise CalculatorError("Division by zero is undefined.")
        except ValueError as exc:
            raise CalculatorError(str(exc)) from exc
        self._history.append(self._value)
        return self

    # ── Basic arithmetic ─────────────────────────────────────────────────────

    def add(self, n: Number) -> "Calculator":
        """Add n to the current value."""
        return self._apply(operator.add, n)

    def subtract(self, n: Number) -> "Calculator":
        """Subtract n from the current value."""
        return self._apply(operator.sub, n)

    def multiply(self, n: Number) -> "Calculator":
        """Multiply the current value by n."""
        return self._apply(operator.mul, n)

    def divide(self, n: Number) -> "Calculator":
        """Divide the current value by n."""
        if n == 0:
            raise CalculatorError("Division by zero is undefined.")
        return self._apply(operator.truediv, n)

    def modulo(self, n: Number) -> "Calculator":
        """Return remainder of dividing current value by n."""
        if n == 0:
            raise CalculatorError("Modulo by zero is undefined.")
        return self._apply(operator.mod, n)

    def power(self, exp: Number) -> "Calculator":
        """Raise current value to the power of exp."""
        return self._apply(operator.pow, exp)

    def negate(self) -> "Calculator":
        """Negate the current value."""
        return self._apply(operator.neg)

    def abs(self) -> "Calculator":
        """Take the absolute value."""
        return self._apply(operator.abs)

    # ── Scientific ───────────────────────────────────────────────────────────

    def sqrt(self) -> "Calculator":
        """Square root of current value."""
        if self._value < 0:
            raise CalculatorError(f"Cannot take sqrt of negative number {self._value}.")
        return self._apply(math.sqrt)

    def log(self, base: Number = math.e) -> "Calculator":
        """Logarithm with given base (default: natural log)."""
        if self._value <= 0:
            raise CalculatorError("Logarithm undefined for non-positive values.")
        if base == math.e:
            return self._apply(math.log)
        return self._apply(lambda x: math.log(x, base))

    def log10(self) -> "Calculator":
        """Base-10 logarithm."""
        return self.log(10)

    def sin(self) -> "Calculator":
        """Sine (radians)."""
        return self._apply(math.sin)

    def cos(self) -> "Calculator":
        """Cosine (radians)."""
        return self._apply(math.cos)

    def tan(self) -> "Calculator":
        """Tangent (radians)."""
        return self._apply(math.tan)

    def exp(self) -> "Calculator":
        """e raised to current value."""
        return self._apply(math.exp)

    def floor(self) -> "Calculator":
        """Round down."""
        return self._apply(math.floor)

    def ceil(self) -> "Calculator":
        """Round up."""
        return self._apply(math.ceil)

    def round_to(self, decimals: int = 0) -> "Calculator":
        """Round to given decimal places."""
        return self._apply(lambda x: round(x, decimals))

    def percent(self) -> "Calculator":
        """Divide by 100."""
        return self._apply(lambda x: x / 100)

    # ── Memory ───────────────────────────────────────────────────────────────

    def mem_store(self) -> "Calculator":
        self._memory = self._value
        return self

    def mem_recall(self) -> "Calculator":
        self._value = self._memory
        self._history.append(self._value)
        return self

    def mem_add(self) -> "Calculator":
        self._memory += self._value
        return self

    def mem_clear(self) -> "Calculator":
        self._memory = 0.0
        return self

    # ── History & reset ──────────────────────────────────────────────────────

    def undo(self) -> "Calculator":
        if len(self._history) < 2:
            raise CalculatorError("Nothing to undo.")
        self._history.pop()
        self._value = self._history[-1]
        return self

    def reset(self, value: Number = 0) -> "Calculator":
        self._value = float(value)
        self._history = [self._value]
        return self

    def clear_history(self) -> "Calculator":
        self._history = [self._value]
        return self

    # ── Expression evaluator ─────────────────────────────────────────────────

    def expr(self, expression: str) -> float:
        """Safely evaluate a plain-text math expression."""
        safe_names = {
            "abs": abs, "round": round,
            "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "exp": math.exp, "floor": math.floor, "ceil": math.ceil,
            "pi": math.pi, "e": math.e,
        }
        try:
            result = eval(expression, {"__builtins__": {}}, safe_names)
        except ZeroDivisionError:
            raise CalculatorError("Division by zero in expression.")
        except Exception as exc:
            raise CalculatorError(f"Invalid expression: {exc}") from exc
        self._value = float(result)
        self._history.append(self._value)
        return self.result

    # ── Utility ──────────────────────────────────────────────────────────────

    def summary(self) -> str:
        lines = [
            "┌─────────────────────────────┐",
            f"│  Result  : {self.result:<18} │",
            f"│  Memory  : {self._memory:<18} │",
            f"│  Steps   : {len(self._history):<18} │",
            "└─────────────────────────────┘",
        ]
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Calculator(result={self.result}, steps={len(self._history)})"

    def __float__(self) -> float:
        return self._value

    def __int__(self) -> int:
        return int(self._value)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Calculator):
            return self._value == other._value
        if isinstance(other, (int, float)):
            return self._value == float(other)
        return NotImplemented

    # ── Static helpers ────────────────────────────────────────────────────────

    @staticmethod
    def compute(expression: str) -> float:
        """One-shot: evaluate expression and return result."""
        return Calculator().expr(expression)

    @staticmethod
    def gcd(a: int, b: int) -> int:
        return math.gcd(int(a), int(b))

    @staticmethod
    def lcm(a: int, b: int) -> int:
        return abs(int(a) * int(b)) // math.gcd(int(a), int(b))

    @staticmethod
    def clamp(value: Number, lo: Number, hi: Number) -> Number:
        return max(lo, min(hi, value))

    @staticmethod
    def percentage_of(part: Number, whole: Number) -> float:
        if whole == 0:
            raise CalculatorError("Whole cannot be zero.")
        return (part / whole) * 100

    @staticmethod
    def solve_quadratic(a: Number, b: Number, c: Number) -> Tuple[complex, complex]:
        """Solve ax² + bx + c = 0. Returns (x1, x2)."""
        discriminant = b**2 - 4 * a * c
        if discriminant >= 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        else:
            real = -b / (2 * a)
            imag = math.sqrt(-discriminant) / (2 * a)
            x1 = complex(real, imag)
            x2 = complex(real, -imag)
        return x1, x2