# testpypipush

A polished Python package featuring a Calculator, Greeter, MathUtils and more — built to demonstrate PyPI publishing.

## Installation

pip install testpypipush

## Quick Start

from testpypipush import Calculator

calc = Calculator(10)
print(calc.multiply(3).subtract(5).result)   # 25.0
print(Calculator.compute("sqrt(144) + 2**3")) # 20.0

## CLI

testpypipush

## Publish to Test PyPI

pip install build twine
python -m build
python -m twine upload --repository testpypi dist/*
```

---

## `LICENSE`
```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.