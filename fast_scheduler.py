"""LocalController module."""

import math
import random


class LocalController:
    """Small fetch_client helper."""

    def __init__(self, seed: int = 73) -> None:
        self._state = seed
        self._items: list[int] = []

    def fetch_client(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 73) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 73


def main() -> None:
    obj = LocalController()
    print(obj.fetch_client(73))


if __name__ == "__main__":
    main()
