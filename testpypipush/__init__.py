"""
testpypipush
────────────
A polished Python package demonstrating PyPI publishing,
featuring a full-featured Calculator, Greeter, MathUtils,
and utility helpers.
"""

__version__ = "0.2.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__license__ = "MIT"

from .calculator import Calculator, CalculatorError
from .core import Greeter, MathUtils
from .utils import format_message, validate_input, chunk_list, flatten

__all__ = [
    "Calculator",
    "CalculatorError",
    "Greeter",
    "MathUtils",
    "format_message",
    "validate_input",
    "chunk_list",
    "flatten",
]