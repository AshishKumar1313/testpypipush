"""
__main__.py
───────────
Run the interactive calculator from the command line:

    python -m testpypipush
    # or, after pip install:
    testpypipush
"""

from __future__ import annotations
import sys
from .calculator import Calculator, CalculatorError
from . import __version__

BANNER = r"""
  ╔══════════════════════════════════════════╗
  ║   testpypipush  ·  Calculator  v{ver:<8}  ║
  ╠══════════════════════════════════════════╣
  ║  Commands                                ║
  ║  ─────────────────────────────────────   ║
  ║  <expr>   evaluate any math expression   ║
  ║  history  show step history              ║
  ║  reset    reset to 0                     ║
  ║  undo     undo last step                 ║
  ║  mem      show memory value              ║
  ║  ms       store result in memory         ║
  ║  mr       recall memory                  ║
  ║  mc       clear memory                   ║
  ║  help     show this help                 ║
  ║  exit     quit                           ║
  ╚══════════════════════════════════════════╝
""".format(ver=__version__)


def _format_history(hist: list) -> str:
    if not hist:
        return "  (empty)"
    lines = []
    for i, v in enumerate(hist):
        marker = "▶" if i == len(hist) - 1 else " "
        lines.append(f"  {marker} [{i:>3}]  {v}")
    return "\n".join(lines)


def main() -> None:
    calc = Calculator()
    print(BANNER)
    print(f"  Starting value: 0\n")

    while True:
        try:
            raw = input("  calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Bye! 👋")
            sys.exit(0)

        if not raw:
            continue

        cmd = raw.lower()

        if cmd in ("exit", "quit", "q"):
            print("  Bye! 👋")
            break
        elif cmd in ("help", "h", "?"):
            print(BANNER)
        elif cmd == "history":
            print(_format_history(calc.history))
        elif cmd == "reset":
            calc.reset()
            print("  → Reset to 0")
        elif cmd == "undo":
            try:
                calc.undo()
                print(f"  → {calc.result}")
            except CalculatorError as e:
                print(f"  ✗ {e}")
        elif cmd == "mem":
            print(f"  Memory: {calc.memory}")
        elif cmd == "ms":
            calc.mem_store()
            print(f"  Memory ← {calc.result}")
        elif cmd == "mr":
            calc.mem_recall()
            print(f"  → {calc.result}")
        elif cmd == "mc":
            calc.mem_clear()
            print("  Memory cleared.")
        else:
            try:
                result = calc.expr(raw)
                print(f"  → {result}")
            except CalculatorError as e:
                print(f"  ✗ {e}")
            except Exception as e:
                print(f"  ✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()