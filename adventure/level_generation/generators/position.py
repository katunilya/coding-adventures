import random
from enum import Enum
from typing import Callable, Iterable

from adventure.level_generation.base import Position2, Ratio2, Size2
from adventure.level_generation.distance import (
    DistanceFunction2,
)
from adventure.level_generation.errors import (
    GenerationFailureError,
    InvalidCountError,
    InvalidPosition2GeneratorKind,
    InvalidRadiusError,
    InvalidSize2AreaError,
)
from adventure.level_generation.utils import (
    get_rectangle_area,
    get_size2_area,
    get_square_area,
    iter_positions,
)

type Position2Generator = Callable[[], Iterable[Position2]]


def naive_position2_generator(
    count: int,
    size: Size2,
    **_,
) -> Position2Generator:
    if count <= 0:
        raise InvalidCountError(count, must_be="gt")

    _area = get_size2_area(size)
    if count > _area:
        raise InvalidCountError(count, must_be="lt", target=_area)

    def _generator() -> Iterable[Position2]:
        _available_positions = set(iter_positions(size))

        for _ in range(count):
            _picked_position = random.choice(list(_available_positions))
            _available_positions.remove(_picked_position)

            yield _picked_position

    return _generator


def min_distance_position2_generator(
    count: int,
    size: Size2,
    min_distance: float,
    distance_function: DistanceFunction2,
    **_,
) -> Position2Generator:
    if count <= 0:
        raise InvalidCountError(count, must_be="gr")

    _area = get_size2_area(size)
    if count > _area:
        raise InvalidCountError(count, must_be="lt", target=_area)

    _min_area = count * get_square_area(min_distance)
    if _min_area > _area:
        raise InvalidSize2AreaError(size, must_be="get", target=_min_area)

    def _generator() -> Iterable[Position2]:
        _available_positions = set(iter_positions(size))

        for _ in range(count):
            if len(_available_positions) == 0:
                raise GenerationFailureError("no position2 to pick from")

            _picked_position = random.choice(list(_available_positions))
            _positions_to_remove = set[Position2](_picked_position)

            for _position in _available_positions:
                if distance_function(_position, _picked_position) <= min_distance:
                    _positions_to_remove.add(_position)

            _available_positions -= _positions_to_remove

            yield _picked_position

    return _generator


def _iter_count_ratios(count: int) -> Iterable[Ratio2]:
    for _del in range(1, count + 1):
        if count % _del == 0:
            yield _del, count // _del


def _get_best_ratio(count: int, target: Ratio2) -> Ratio2:
    _result = (-1, -1)
    _min_diff = float("inf")

    _target_rc = target[0] / target[1]

    for _ratio in _iter_count_ratios(count):
        _current_rc = _ratio[0] / _ratio[1]
        _current_diff = abs(_target_rc - _current_rc)

        if _current_diff < _min_diff:
            _min_diff = _current_diff
            _result = _ratio

    return _result


def grid_position2_generator(
    count: int,
    size: Size2,
    **_,
) -> Position2Generator:
    if count <= 0:
        raise InvalidCountError(count, must_be="gt")

    _size_area = get_size2_area(size)
    _max_row, _max_col = size
    _row_count, _col_count = _get_best_ratio(count, size)
    _row_size, _col_size = _max_row / _row_count, _max_col / _col_count
    _required_area = get_rectangle_area(_row_size, _col_size)

    if _required_area > _size_area:
        raise InvalidSize2AreaError(size, must_be="get", target=_required_area)

    def _generator() -> Iterable[Position2]:
        for _r in range(_row_count):
            for _c in range(_col_count):
                _row = int((_r * _row_size) + _row_size / 2)
                _col = int((_c * _col_size) + _col_size / 2)
                yield _row, _col

    return _generator


def fuzzy_grid_position2_generator(
    count: int,
    size: Size2,
    fuzz_radius: float | None = None,
    **_,
) -> Position2Generator:
    _max_row, _max_col = size
    _row_count, _col_count = _get_best_ratio(count, size)
    _row_size, _col_size = _max_row / _row_count, _max_col / _col_count

    if fuzz_radius is None:
        fuzz_radius = min(_row_size, _col_size)
    else:
        _min_target = min(_row_size, _col_size)
        if fuzz_radius > _min_target:
            raise InvalidRadiusError(fuzz_radius, must_be="let", target=_min_target)

    _grid_generator = grid_position2_generator(count, size)

    def _generator() -> Iterable[Position2]:
        for _row, _col in _grid_generator():
            _row_shift = random.uniform(-fuzz_radius, fuzz_radius)
            _col_shift = random.uniform(-fuzz_radius, fuzz_radius)

            yield int(_row + _row_shift), int(_col + _col_shift)

    return _generator


class Position2GeneratorKind(str, Enum):
    NAIVE = "naive"
    MIN_DISTANCE = "min-distance"
    GRID = "grid"
    FUZZY_GRID = "fuzzy-grid"


_POSITION2_GENERATOR_DICT = {
    Position2GeneratorKind.NAIVE.value: naive_position2_generator,
    Position2GeneratorKind.MIN_DISTANCE.value: min_distance_position2_generator,
    Position2GeneratorKind.GRID.value: grid_position2_generator,
    Position2GeneratorKind.FUZZY_GRID.value: fuzzy_grid_position2_generator,
}


def get_position2_generator(
    kind: Position2GeneratorKind | str, **kwargs
) -> Position2Generator:
    _key = kind.value if isinstance(kind, Position2GeneratorKind) else kind

    if _key not in _POSITION2_GENERATOR_DICT:
        raise InvalidPosition2GeneratorKind(_key)

    return _POSITION2_GENERATOR_DICT[_key](**kwargs)
