from typing import TypeVar, Optional, Generic
from abc import ABCMeta, abstractmethod

T = TypeVar("T")


class Folder(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def boolean(self, preset: Optional[bool] = None) -> T:
        raise NotImplementedError

    @abstractmethod
    def string(self) -> T:
        raise NotImplementedError

    @abstractmethod
    def integer(self) -> T:
        raise NotImplementedError
    
    @abstractmethod
    def float(self) -> T:
        raise NotImplementedError

    @abstractmethod
    def array_of(self, argument: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def ref(self, tp: str) -> T:
        raise NotImplementedError


class StringFolder(Folder[str]):
    __slots__ = ("legacy_bindings",)

    def __init__(self, legacy_bindings: bool) -> None:
        self.legacy_bindings = legacy_bindings

    def ref(self, tp: str) -> str:
        return tp

    def boolean(self, preset: Optional[bool] = None) -> str:
        if preset is not None:
            return str(preset)
        return "bool"

    def string(self) -> str:
        return "str"
    
    def float(self) -> str:
        return "float"

    def integer(self) -> str:
        return "int"

    def array_of(self, argument: str) -> str:
        if self.legacy_bindings:
            return f"List[{argument}]"
        return f"list[{argument}]"
