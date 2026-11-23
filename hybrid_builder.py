"""SmartParser module."""

import math
import random


class SmartParser:
    """Small run_context helper."""

    def __init__(self, seed: int = 5) -> None:
        self._state = seed
        self._items: list[int] = []

    def run_context(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 5) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 5


def main() -> None:
    obj = SmartParser()
    print(obj.run_context(5))


if __name__ == "__main__":
    main()
