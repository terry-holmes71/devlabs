"""SmartController module."""

import math
import random


class SmartController:
    """Small compute_cache helper."""

    def __init__(self, seed: int = 54) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_cache(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 54) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 54


def main() -> None:
    obj = SmartController()
    print(obj.compute_cache(54))


if __name__ == "__main__":
    main()
