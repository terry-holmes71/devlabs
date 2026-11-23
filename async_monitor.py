"""SecureCache module."""

import math
import random


class SecureCache:
    """Small run_handler helper."""

    def __init__(self, seed: int = 97) -> None:
        self._state = seed
        self._items: list[int] = []

    def run_handler(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 97) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 97


def main() -> None:
    obj = SecureCache()
    print(obj.run_handler(97))


if __name__ == "__main__":
    main()
