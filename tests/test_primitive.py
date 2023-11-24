from telegram_type_parser import parse


def test_integer() -> None:
    assert parse("Integer") == "int"


def test_string() -> None:
    assert parse("String") == "str"


def test_boolean() -> None:
    assert parse("Boolean") == "bool"
    assert parse("True") == "True"
    assert parse("False") == "False"
