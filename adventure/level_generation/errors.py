from dataclasses import dataclass
from typing import Literal, Protocol

from adventure.level_generation.base import Position2, Size2


class Error(Protocol):
    def as_str(self) -> str: ...


@dataclass(slots=True, frozen=True, eq=True)
class InvalidPosition2Error(Error, Exception):
    position: Position2
    limits: Size2

    def as_str(self) -> str:
        return f"invalid position2: {self.position} not in limits {self.limits}"


type NumberConstraint = Literal["gt", "get", "lt", "let"]

_NUMBER_CONSTRAINT_TO_OPERATOR = {
    "gt": ">",
    "get": ">=",
    "lt": "<",
    "let": "<=",
}


@dataclass(slots=True, frozen=True, eq=True)
class InvalidCountError(Error, Exception):
    count: int
    must_be: NumberConstraint = "gt"
    target: int = 0

    def as_str(self) -> str:
        _operator = _NUMBER_CONSTRAINT_TO_OPERATOR[self.must_be]
        return f"invalid count: {self.count} must be {_operator} {self.target}"


@dataclass(slots=True, frozen=True, eq=True)
class InvalidDistanceError(Error, Exception):
    distance: float
    must_be: NumberConstraint = "get"
    target: float = 0.0

    def as_str(self) -> str:
        _operator = _NUMBER_CONSTRAINT_TO_OPERATOR[self.must_be]
        return f"invalid count: {self.count} must be {_operator} {self.target}"


@dataclass(slots=True, frozen=True, eq=True)
class InvalidRadiusError(Error, Exception):
    radius: float
    must_be: NumberConstraint = "get"
    target: float = 0.0

    def as_str(self) -> str:
        _operator = _NUMBER_CONSTRAINT_TO_OPERATOR[self.must_be]
        return f"invalid radius: {self.count} must be {_operator} {self.target}"


@dataclass(slots=True, frozen=True, eq=True)
class InvalidSize2AreaError(Error, Exception):
    size: Size2
    must_be: NumberConstraint
    target: float

    def as_str(self) -> str:
        _operator = _NUMBER_CONSTRAINT_TO_OPERATOR[self.must_be]
        return (
            f"invalid size2 area: area {self.size[0] * self.size[1]} of {self.size} "
            f"must be {_operator} {self.target}"
        )


@dataclass(slots=True, frozen=True, eq=True)
class InvalidPosition2GeneratorKind(Error, Exception):
    kind: str

    def as_str(self) -> str:
        return f"invalid position2 generator kind: {self.kind}"


@dataclass(slots=True, frozen=True, eq=True)
class InvalidDistanceFunction2Kind(Error, Exception):
    kind: str

    def as_str(self) -> str:
        return f"invalid distance function 2 kind: {self.kind}"


@dataclass(slots=True, frozen=True, eq=True)
class GenerationFailureError(Error):
    reason: str

    def as_str(self) -> str:
        return f"generation failure: {self.reason}"
