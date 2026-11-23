"""AtomicGateway module."""

import math
import random


class AtomicGateway:
    """Small flush_service helper."""

    def __init__(self, seed: int = 21) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_service(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 21) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 21


def main() -> None:
    obj = AtomicGateway()
    print(obj.flush_service(21))


if __name__ == "__main__":
    main()
