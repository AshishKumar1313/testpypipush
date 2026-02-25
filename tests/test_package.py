"""
Tests for Greeter, MathUtils, and utils.
"""

import pytest
from testpypipush import Greeter, MathUtils, format_message, validate_input
from testpypipush.utils import chunk_list, flatten


class TestGreeter:
    def test_default_name(self):
        assert Greeter().name == "World"

    def test_custom_name(self):
        assert Greeter("Alice").name == "Alice"

    def test_casual_greet(self):
        assert Greeter("Bob").greet("casual") == "Hey, Bob!"

    def test_formal_greet(self):
        assert Greeter("Bob").greet("formal") == "Good day, Bob."

    def test_excited_greet(self):
        assert "Bob" in Greeter("Bob").greet("excited")

    def test_invalid_style(self):
        with pytest.raises(ValueError):
            Greeter("Bob").greet("unknown")

    def test_farewell(self):
        assert "Carol" in Greeter("Carol").farewell()

    def test_invalid_name_type(self):
        with pytest.raises(TypeError):
            Greeter(123)

    def test_empty_name(self):
        with pytest.raises(ValueError):
            Greeter("  ")


class TestMathUtils:
    def test_add(self):
        assert MathUtils.add(2, 3) == 5

    def test_subtract(self):
        assert MathUtils.subtract(10, 4) == 6

    def test_multiply(self):
        assert MathUtils.multiply(3, 4) == 12

    def test_divide(self):
        assert MathUtils.divide(10, 2) == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            MathUtils.divide(5, 0)

    def test_factorial_zero(self):
        assert MathUtils.factorial(0) == 1

    def test_factorial_positive(self):
        assert MathUtils.factorial(5) == 120

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            MathUtils.factorial(-1)

    def test_is_prime_true(self):
        for p in [2, 3, 5, 7, 11]:
            assert MathUtils.is_prime(p)

    def test_is_prime_false(self):
        for n in [0, 1, 4, 6, 9]:
            assert not MathUtils.is_prime(n)

    def test_fibonacci(self):
        assert MathUtils.fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


class TestUtils:
    def test_format_message(self):
        assert format_message("  hello  ") == "hello"

    def test_format_message_type_error(self):
        with pytest.raises(TypeError):
            format_message(42)

    def test_validate_input_ok(self):
        validate_input("hello", str, "test")

    def test_validate_input_type_error(self):
        with pytest.raises(TypeError):
            validate_input(42, str, "test")

    def test_validate_input_empty_str(self):
        with pytest.raises(ValueError):
            validate_input("  ", str, "test")

    def test_chunk_list(self):
        assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_chunk_list_invalid_size(self):
        with pytest.raises(ValueError):
            chunk_list([1, 2, 3], 0)

    def test_flatten(self):
        assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]