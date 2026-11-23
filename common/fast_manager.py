"""AtomicHandler module."""

import math
import random


class AtomicHandler:
    """Small handle_manager helper."""

    def __init__(self, seed: int = 5) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_manager(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 5) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 5


def main() -> None:
    obj = AtomicHandler()
    print(obj.handle_manager(5))


if __name__ == "__main__":
    main()
