from __future__ import annotations

import math
from enum import Enum
from typing import Callable

from adventure.level_generation.errors import InvalidDistanceFunction2Kind
from adventure.level_generation.level import Position2

type DistanceFunction2 = Callable[[Position2, Position2], float]


def euler2(first: Position2, second: Position2) -> float:
    return math.sqrt((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2)


def manhattan2(first: Position2, second: Position2) -> float:
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def taxicab2(first: Position2, second: Position2) -> float:
    return manhattan2(first, second)


def chebyshev2(first: Position2, second: Position2) -> float:
    return max(abs(first[0] - second[0]), abs(first[1] - second[1]))


class DistanceFunction2Kind(str, Enum):
    EULER = "euler"
    MANHATTAN = "manhattan"
    TAXICAB = "taxicab"
    CHEBYSHEV = "chebyshev"


_DISTANCE_FUNCTION2_DICT = {
    DistanceFunction2Kind.EULER.value: euler2,
    DistanceFunction2Kind.MANHATTAN.value: manhattan2,
    DistanceFunction2Kind.TAXICAB.value: taxicab2,
    DistanceFunction2Kind.CHEBYSHEV.value: chebyshev2,
}


def get_distance_function2(kind: DistanceFunction2Kind | str) -> DistanceFunction2:
    _key = kind.value if isinstance(kind, DistanceFunction2Kind) else kind

    if _key not in _DISTANCE_FUNCTION2_DICT:
        raise InvalidDistanceFunction2Kind(_key)

    return _DISTANCE_FUNCTION2_DICT[_key]
