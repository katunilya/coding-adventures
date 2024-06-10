from copy import deepcopy
from dataclasses import dataclass, field
from typing import Any, Self

from adventure.level_generation.base import Position2, Size2
from adventure.level_generation.errors import InvalidPosition2Error
from adventure.level_generation.utils import is_inside


@dataclass(slots=True)
class Level2[_TTile]:
    size: Size2
    default: _TTile
    _data: list[list[_TTile]] = field(init=False, default_factory=list)

    def __post_init__(self) -> None:
        self.clear()

    def clear(self) -> Self:
        self._data = []
        _rows, _cols = self.size

        for _row in range(_rows):
            self._data.append([])
            for _ in range(_cols):
                self._data[_row].append(deepcopy(self.default))

        return self

    def get_at(self, position: Position2) -> _TTile:
        if not is_inside(position, self.size):
            raise InvalidPosition2Error(position, self.size)

        _r, _c = position
        return self._data[_r][_c]

    def set_at(self, position: Position2, value: _TTile) -> Self:
        if not is_inside(position, self.size):
            raise InvalidPosition2Error(position, self.size)

        _r, _c = position
        self._data[_r][_c] = value

        return self

    def as_dict(self) -> dict[str, Any]:
        return {
            "size": list(self.size),
            "default_type": type(self.default).__name__,
            "data": self._data,
        }
