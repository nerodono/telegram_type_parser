from typing import Optional, Callable
from telegram_type_parser import fold_ex, Folder


# IDK what to type so be it
class AsArray(Folder[int | list[int]]):
    def string(self) -> int | list[int]:
        return 0

    def integer(self) -> int | list[int]:
        return 1

    def boolean(self, preset: Optional[bool] = None) -> int | list[int]:
        if preset is None:
            return 2
        return 3 + preset

    def ref(self, tp: str) -> int | list[int]:
        return [0, int.from_bytes(tp.encode(), "little")]

    def array_of(self, argument: Callable[[], int | list[int]]):
        return [1, argument()]


tps = [
    "Array of Message",
    "Array of Array of Message",
    "Integer",
    "String",
    "Boolean",
]

creepycode = AsArray()
for tp in tps:
    print(tp, "is", fold_ex(tp, creepycode))

# Expected output is:
# Array of Message is [1, [0, 28542640894207309]]
# Array of Array of Message is [1, [1, [0, 28542640894207309]]]
# Integer is 1
# String is 0
# Boolean is 2
