"""SmartRouter module."""

import math
import random


class SmartRouter:
    """Small compute_provider helper."""

    def __init__(self, seed: int = 39) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_provider(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 39) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 39


def main() -> None:
    obj = SmartRouter()
    print(obj.compute_provider(39))


if __name__ == "__main__":
    main()
