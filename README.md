# telegram-type-parser

Library that simply parses telegram types, for example:

- `Integer`: parses as `int`
- `String`: `str`
- `Boolean`: `bool`
- `True`: `True`
- `False`: `False`
- `Array of <tail>`: as `list[<tail>]` (parsed recursively, for example: `Array of Array of Integer` would be `list[list[int]]`)
- Others are kept as-is (considered composite types)

## Quickstart

```python
from telegram_type_parser import parse

tps = [
    "Array of Message",
    "Array of Array of Message",
    "Integer",
    "String",
    "Boolean",
]

for tp in tps:
    print(tp, "is", parse(tp))

# Expected output is:
# Array of Message is list[Message]
# Array of Array of Message is list[list[Message]]
# Integer is int
# String is str
# Boolean is bool
```

## Need more?

We have more. If you translating telegram types into something that is not the python type hints, then use `telegram_type_parser.parse_ex` and pass custom `Folder` to it, for example:

```python
from typing import Optional, Callable
from telegram_type_parser import parse_ex, Folder


# IDK what to type so example is pretty made up
class AsArray(Folder[int | list[int]]):
    def string(self) -> int | list[int]:
        return 0

    def integer(self) -> int | list[int]:
        return 1

    def boolean(self, preset: Optional[bool] = None) -> int | list[int]:
        if preset is None:
            return 2
        return 3 + preset

    def composite(self, tp: str) -> int | list[int]:
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
    print(tp, "is", parse_ex(tp, creepycode))

# Expected output is:
# Array of Message is [1, [0, 28542640894207309]]
# Array of Array of Message is [1, [1, [0, 28542640894207309]]]
# Integer is 1
# String is 0
# Boolean is 2
```
