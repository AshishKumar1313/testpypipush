"""
Tests for the Calculator class.
"""

import math
import pytest
from testpypipush.calculator import Calculator, CalculatorError


class TestConstruction:
    def test_default_initial(self):
        assert Calculator().result == 0

    def test_custom_initial(self):
        assert Calculator(42).result == 42

    def test_float_initial(self):
        assert Calculator(3.14).result == 3.14

    def test_negative_initial(self):
        assert Calculator(-7).result == -7


class TestArithmetic:
    def test_add(self):
        assert Calculator(5).add(3).result == 8

    def test_subtract(self):
        assert Calculator(10).subtract(4).result == 6

    def test_multiply(self):
        assert Calculator(6).multiply(7).result == 42

    def test_divide(self):
        assert Calculator(10).divide(4).result == 2.5

    def test_divide_by_zero(self):
        with pytest.raises(CalculatorError, match="zero"):
            Calculator(5).divide(0)

    def test_modulo(self):
        assert Calculator(10).modulo(3).result == 1

    def test_modulo_by_zero(self):
        with pytest.raises(CalculatorError):
            Calculator(5).modulo(0)

    def test_power(self):
        assert Calculator(2).power(10).result == 1024

    def test_negate(self):
        assert Calculator(7).negate().result == -7

    def test_abs_negative(self):
        assert Calculator(-5).abs().result == 5


class TestChaining:
    def test_basic_chain(self):
        assert Calculator(10).multiply(3).subtract(5).result == 25

    def test_long_chain(self):
        assert Calculator(1).add(1).multiply(2).add(1).multiply(2).result == 10

    def test_chain_returns_self(self):
        c = Calculator()
        assert c.add(1) is c


class TestScientific:
    def test_sqrt(self):
        assert Calculator(16).sqrt().result == 4

    def test_sqrt_negative(self):
        with pytest.raises(CalculatorError):
            Calculator(-1).sqrt()

    def test_log_natural(self):
        assert abs(Calculator(math.e).log().result - 1.0) < 1e-9

    def test_log10(self):
        assert abs(Calculator(100).log10().result - 2.0) < 1e-9

    def test_sin_zero(self):
        assert abs(Calculator(0).sin().result) < 1e-9

    def test_cos_zero(self):
        assert abs(Calculator(0).cos().result - 1.0) < 1e-9

    def test_exp(self):
        assert abs(Calculator(1).exp().result - math.e) < 1e-9

    def test_floor(self):
        assert Calculator(3.7).floor().result == 3

    def test_ceil(self):
        assert Calculator(3.2).ceil().result == 4

    def test_round_to(self):
        assert Calculator(3.14159).round_to(2).result == 3.14

    def test_percent(self):
        assert Calculator(50).percent().result == 0.5


class TestHistory:
    def test_initial_history(self):
        assert Calculator(5).history == [5.0]

    def test_history_grows(self):
        c = Calculator(0).add(1).add(2).add(3)
        assert c.history == [0.0, 1.0, 3.0, 6.0]

    def test_undo(self):
        c = Calculator(0).add(10).add(5)
        c.undo()
        assert c.result == 10

    def test_undo_nothing(self):
        with pytest.raises(CalculatorError, match="Nothing to undo"):
            Calculator().undo()

    def test_reset(self):
        c = Calculator(100).add(50).reset()
        assert c.result == 0
        assert c.history == [0.0]

    def test_clear_history(self):
        c = Calculator(5).add(3).clear_history()
        assert c.history == [8.0]


class TestMemory:
    def test_mem_default(self):
        assert Calculator().memory == 0.0

    def test_mem_store_recall(self):
        c = Calculator(42).mem_store().reset().mem_recall()
        assert c.result == 42

    def test_mem_add(self):
        c = Calculator(10).mem_store().reset(5).mem_add()
        assert c.memory == 15

    def test_mem_clear(self):
        c = Calculator(99).mem_store().mem_clear()
        assert c.memory == 0.0


class TestExpr:
    def test_simple_add(self):
        assert Calculator().expr("3 + 4") == 7

    def test_compound(self):
        assert Calculator().expr("(3 + 4) * 2") == 14

    def test_power(self):
        assert Calculator().expr("2 ** 8") == 256

    def test_sqrt_func(self):
        assert Calculator().expr("sqrt(25)") == 5.0

    def test_pi_constant(self):
        assert abs(Calculator().expr("pi * 2") - 2 * math.pi) < 1e-9

    def test_invalid_expr(self):
        with pytest.raises(CalculatorError):
            Calculator().expr("import os")

    def test_static_compute(self):
        assert Calculator.compute("100 / 4") == 25.0


class TestStaticHelpers:
    def test_gcd(self):
        assert Calculator.gcd(12, 8) == 4

    def test_lcm(self):
        assert Calculator.lcm(4, 6) == 12

    def test_clamp_within(self):
        assert Calculator.clamp(5, 0, 10) == 5

    def test_clamp_below(self):
        assert Calculator.clamp(-5, 0, 10) == 0

    def test_clamp_above(self):
        assert Calculator.clamp(15, 0, 10) == 10

    def test_percentage_of(self):
        assert Calculator.percentage_of(25, 200) == 12.5

    def test_quadratic_real_roots(self):
        x1, x2 = Calculator.solve_quadratic(1, -5, 6)
        assert sorted([x1, x2]) == [2.0, 3.0]

    def test_quadratic_complex_roots(self):
        x1, x2 = Calculator.solve_quadratic(1, 0, 1)
        assert isinstance(x1, complex)


class TestDunders:
    def test_float(self):
        assert float(Calculator(3.5)) == 3.5

    def test_int(self):
        assert int(Calculator(3.9)) == 3

    def test_eq_number(self):
        assert Calculator(5) == 5

    def test_repr(self):
        assert "10" in repr(Calculator(7).add(3))

    def test_summary(self):
        s = Calculator(42).summary()
        assert "42" in s