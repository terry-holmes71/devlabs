"""BatchCollector module."""

import math
import random


class BatchCollector:
    """Small collect_loader helper."""

    def __init__(self, seed: int = 95) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_loader(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 95) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 95


def main() -> None:
    obj = BatchCollector()
    print(obj.collect_loader(95))


if __name__ == "__main__":
    main()
