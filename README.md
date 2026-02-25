# 🧮 testpypipush

> A polished Python package featuring a **Calculator**, **Greeter**, **MathUtils** and more — built to demonstrate PyPI publishing.

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-86%20passing-brightgreen)
![PyPI](https://img.shields.io/badge/TestPyPI-0.2.0-orange)

---

## 📦 Installation
```bash
pip install --index-url https://test.pypi.org/simple/ testpypipush-as
```

---

## ✨ Features

| Module | Description |
|--------|-------------|
| 🧮 `Calculator` | Stateful calculator with chaining, history, memory & scientific ops |
| 👋 `Greeter` | Multi-style greeting helper |
| 📐 `MathUtils` | Fibonacci, primes, factorial and more |
| 🔧 `utils` | Input validation, list chunking, flattening |
| ⌨️ CLI | Interactive calculator REPL |

---

## 🚀 Quick Start

### Calculator
```python
from testpypipush import Calculator

# Basic chaining
calc = Calculator(10)
print(calc.multiply(3).subtract(5).result)   # 25.0

# Expression evaluator
print(Calculator.compute("sqrt(144) + 2**3"))  # 20.0

# Scientific operations
Calculator(16).sqrt().result        # 4.0
Calculator(100).log10().result      # 2.0

# History & undo
c = Calculator(0).add(10).multiply(5)
print(c.history)   # [0.0, 10.0, 50.0]
c.undo()
print(c.result)    # 10.0

# Memory
c = Calculator(99).mem_store().reset().mem_recall()
print(c.result)    # 99.0

# Pretty summary
print(Calculator(42).multiply(2).summary())
# ┌─────────────────────────────┐
# │  Result  : 84.0             │
# │  Memory  : 0.0              │
# │  Steps   : 2                │
# └─────────────────────────────┘
```

### Greeter
```python
from testpypipush import Greeter

g = Greeter("AS")
print(g.greet("casual"))    # Hey, AS!
print(g.greet("formal"))    # Good day, AS.
print(g.greet("excited"))   # WOW, AS!!! 🎉
print(g.farewell())         # Goodbye, AS!
```

### MathUtils
```python
from testpypipush import MathUtils

print(MathUtils.fibonacci(8))    # [0, 1, 1, 2, 3, 5, 8, 13]
print(MathUtils.factorial(10))   # 3628800
print(MathUtils.is_prime(97))    # True
```

---

## ⌨️ CLI — Interactive Calculator
```bash
python -m testpypipush
```
```
  ╔══════════════════════════════════════════╗
  ║   testpypipush  ·  Calculator  v0.2.0    ║
  ╠══════════════════════════════════════════╣
  ║  <expr>   evaluate any math expression   ║
  ║  history  show step history              ║
  ║  undo     undo last step                 ║
  ║  reset    reset to 0                     ║
  ║  exit     quit                           ║
  ╚══════════════════════════════════════════╝

  calc> (3 + 4) * 2
  → 14.0
  calc> sqrt(144) + pi
  → 15.141592653589793
  calc> history
    ▶ [  0]  14.0
       [  1]  15.14
  calc> exit
  Bye! 👋
```

---

## 📁 Project Structure
```
testpypipush/
├── testpypipush/
│   ├── __init__.py       ← public API
│   ├── __main__.py       ← CLI entry point
│   ├── calculator.py     ← Calculator class
│   ├── core.py           ← Greeter & MathUtils
│   └── utils.py          ← helper functions
├── tests/
│   ├── test_calculator.py
│   └── test_package.py
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 🧪 Running Tests
```bash
pip install -e ".[dev]"
python -m pytest
```

Expected output:
```
86 passed in 1.2s ✅
```

---

## 🏗️ Build & Publish
```bash
# Build
pip install build twine
python -m build

# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# Upload to real PyPI
python -m twine upload dist/*
```

---

## 📄 License

MIT License © 2024 [AshishKumar1313](https://github.com/AshishKumar1313)

---

<div align="center">
  Built with ❤️ to demonstrate Python packaging best practices
  <br><br>
  ⭐ Star this repo if you found it helpful!
</div>