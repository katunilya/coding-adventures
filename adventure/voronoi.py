import random
from math import pi, sqrt
from typing import Callable, Iterable

type Position = tuple[int, int]
type Size = tuple[int, int]
type VoronoiMap = list[list[int]]
type DistanceFunction = Callable[[Position, Position], float]
type DistributionFunction = Callable[[Size, int], set[Position]]
type LabeledGroups = dict[Position, int]


def euler_distance(x: Position, y: Position) -> float:
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def manhattan_distance(x: Position, y: Position) -> float:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def chebyshev_distance(x: Position, y: Position) -> float:
    return max(abs(x[0] - y[0]), abs(x[1] - y[1]))


def random_distribution(size: Size, count: int) -> set[Position]:
    _max_row, _max_col = size

    if _max_row * _max_col < count:
        raise ValueError(f"too many groups: {count=}, {size=}")

    _centers = set[Position]()

    while len(_centers) < count:
        _center = (
            random.randint(0, _max_row - 1),
            random.randint(0, _max_col - 1),
        )
        _centers.add(_center)

    return _centers


def min_distance_random_distribution(
    min_distance: float,
    distance_function: DistanceFunction,
) -> DistributionFunction:
    if min_distance < 0:
        raise ValueError(f"invalid min distance: cannot be negative {min_distance=}")

    def _min_distance_random_distribution(size: Size, count: int) -> set[Position]:
        _max_row, _max_col = size

        if _max_row * _max_col < count * (2 * pi * (min_distance**2)):
            raise ValueError(f"too many groups: {count=}, {size=}, {min_distance=}")

        _centers = set[Position]()

        while len(_centers) < count:
            _center = (
                random.randint(0, _max_row - 1),
                random.randint(0, _max_col - 1),
            )

            if all([distance_function(_center, c) >= min_distance for c in _centers]):
                _centers.add(_center)

        return _centers

    return _min_distance_random_distribution


def fuzzy_grid_distribution(
    max_fuzz_radius: float,
) -> DistributionFunction:
    if max_fuzz_radius < 0.0:
        raise ValueError("invalid fuzz radius: must be positive")

    def _fuzzy_grid_distribution(size: Size, count: int) -> set[Position]:
        _max_row, _max_col = size
        _row_count, _col_count = find_closest_ratio(count, _max_row, _max_col)
        print(_row_count, _col_count)
        _row_size = _max_row / _row_count
        _col_size = _max_col / _col_count

        _aligned_centers = set[tuple[float, float]]()

        for _r in range(_row_count):
            for _c in range(_col_count):
                _aligned_centers.add(
                    (
                        _r * _row_size + (_row_size / 2),
                        _c * _col_size + (_col_size / 2),
                    )
                )

        _centers = set[Position]()

        for _row, _col in _aligned_centers:
            while True:
                _center = (
                    int(_row + random.uniform(-max_fuzz_radius, max_fuzz_radius)),
                    int(_col + random.uniform(-max_fuzz_radius, max_fuzz_radius)),
                )
                if _center not in _centers:
                    _centers.add(_center)
                    break

        return _centers

    return _fuzzy_grid_distribution


def iter_all_int_ratios(num: int) -> Iterable[tuple[int, int]]:
    for _del in range(1, num + 1):
        if num % _del == 0:
            yield (_del, num // _del)


def find_closest_ratio(num: int, first: int, second: int) -> tuple[int, int]:
    _target_ration = first / second
    _result = (-1, -1)
    _min_distance_to_target = float("inf")

    for _first, _second in iter_all_int_ratios(num):
        _current_ration = _first / _second
        _current_distance_to_target = abs(_current_ration - _target_ration)

        if _current_distance_to_target < _min_distance_to_target:
            _result = (_first, _second)
            _min_distance_to_target = _current_distance_to_target

    return _result


def empty_voronoi_map(size: Size) -> VoronoiMap:
    _rows, _cols = size
    _map: VoronoiMap = []

    for _row in range(_rows):
        _map.append([])
        for _ in range(_cols):
            _map[_row].append(-1)

    return _map


def iter_positions(size: Size) -> Iterable[Position]:
    _rows, _cols = size

    for _row in range(_rows):
        for _col in range(_cols):
            yield _row, _col


def set_label(position: Position, map_: VoronoiMap, label: int) -> VoronoiMap:
    _row, _col = position
    map_[_row][_col] = label

    return map_


def propagate_labels(centers: set[Position]) -> LabeledGroups:
    _labeled_groups: LabeledGroups = {}

    for _label, _center in enumerate(centers):
        _labeled_groups[_center] = _label + 1

    return _labeled_groups


def get_closest_label(
    position: Position,
    labeled_groups: LabeledGroups,
    distance_function: DistanceFunction,
) -> int:
    _result_label = -1
    _min_distance = float("inf")

    for _center, _label in labeled_groups.items():
        _distance = distance_function(position, _center)

        if _distance < _min_distance:
            _result_label = _label
            _min_distance = _distance

    return _result_label


def iter_generate(
    size: Size,
    count: int,
    distance_function: DistanceFunction,
    distribution_function: DistributionFunction,
) -> Iterable[VoronoiMap]:
    _map = empty_voronoi_map(size)
    _centers = distribution_function(size, count)
    _labeled_groups = propagate_labels(_centers)

    for _position in iter_positions(size):
        _closest_label = get_closest_label(
            _position,
            _labeled_groups,
            distance_function,
        )

        _map = set_label(_position, _map, _closest_label)

        yield _map


def generate(
    size: Size,
    count: int,
    distance_function: DistanceFunction,
    distribution_function: DistributionFunction,
) -> VoronoiMap:
    return list(
        iter_generate(
            size,
            count,
            distance_function,
            distribution_function,
        )
    )[-1]
