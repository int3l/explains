from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from a import A


class B:
    def __init__(self):
        self.a_items = []

    def baz(self) -> int:
        return 9001

    def register_a(self, a: A) -> None:
        self.a_items.append(a)
