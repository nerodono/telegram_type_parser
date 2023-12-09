from typing import TypeVar
from .folder import Folder, StringFolder

T = TypeVar("T")


def fold_ex(tp: str, folder: Folder[T]) -> T:
    """
    Fold telegram type using specified `folder`
    | `tp`: telegram type
    | `folder`: type that __folds__ types into a single value
    """

    if tp.startswith("Array of"):
        stripped = tp.removeprefix("Array of").lstrip()
        return folder.array_of(fold_ex(stripped, folder))
    elif tp == "Integer":
        return folder.integer()
    elif tp == "String":
        return folder.string()
    elif tp == "Boolean":
        return folder.boolean()
    elif tp == "True":
        return folder.boolean(True)
    elif tp == "False":
        return folder.boolean(False)

    return folder.ref(tp)


def fold(tp: str, legacy_bindings: bool = False) -> str:
    """
    Same as calling `fold_ex` with the `telegram_type_parser.folder.StringFolder` folder
    | `legacy_bindings`: whether to use legacy type hints or not (e.g. List instead of list)
    | `tp`: telegram type
    """
    return fold_ex(tp, StringFolder(legacy_bindings))


__all__ = [
    "parse",
    "parse_ex",
    "Folder",
    "StringFolder",
]
