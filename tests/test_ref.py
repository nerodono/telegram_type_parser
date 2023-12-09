import pytest

from telegram_type_parser import fold


# asserts identity
@pytest.mark.parametrize(
    "input_",
    [
        "SimplyComposite",
        "Photo",
        "Integral",
        "Enumeration",
        "Chat",
    ],
)
def test_simple_composite(input_: str) -> None:
    assert fold(input_) == input_


@pytest.mark.parametrize(
    "input_,expected",
    [
        ("Array of Integer", "list[int]"),
        ("Array of Array of Message", "list[list[Message]]"),
        ("Array of Array of Array of Array of I", "list[list[list[list[I]]]]"),
        ("Array of String", "list[str]"),
        ("Array of Boolean", "list[bool]"),
        ("Array of True", "list[True]"),
        ("Array of False", "list[False]"),
    ],
)
def test_nesting(input_: str, expected: str) -> None:
    assert fold(input_) == expected
