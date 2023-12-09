from telegram_type_parser import fold


def test_integer() -> None:
    assert fold("Integer") == "int"


def test_string() -> None:
    assert fold("String") == "str"


def test_boolean() -> None:
    assert fold("Boolean") == "bool"
    assert fold("True") == "True"
    assert fold("False") == "False"

def test_float() -> None:
    assert fold("Float") == "float"
