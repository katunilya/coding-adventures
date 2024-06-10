import math
from typing import Iterable

from adventure.level_generation.base import Position2, Size2
from adventure.level_generation.errors import InvalidRadiusError


def iter_positions(size: Size2) -> Iterable[Position2]:
    _rows, _cols = size

    for _row in range(_rows):
        for _col in range(_cols):
            yield _row, _col


def is_inside(position: Position2, size: Size2) -> bool:
    return 0 <= position[0] < size[0] and 0 <= position[1] < size[1]


def get_size2_area(size: Size2) -> int:
    return size[0] * size[1]


def get_circle_area(radius: float) -> float:
    if radius < 0.0:
        raise InvalidRadiusError(radius)

    return 2 * math.pi * (radius**2)


def get_square_area(side: float) -> float:
    return side**2


def get_rectangle_area(height: float, width: float) -> float:
    return height * width


def scale_size2(size: Size2, scale: int) -> Size2:
    return size[0] * scale, size[1] * scale
