from typing import Final, Iterable

from tibia import Many

from adventure.level_generation.base import Position2, Size2
from adventure.level_generation.distance import DistanceFunction2
from adventure.level_generation.generators.position import Position2Generator
from adventure.level_generation.level import Level2
from adventure.level_generation.utils import iter_positions

type VoronoiLevel2 = Level2[int]

DEFAULT_TILE: Final = -1


def get_closes_tile(
    position: Position2,
    center_positions_with_labels: dict[Position2, int],
    distance_function: DistanceFunction2,
) -> int:
    _closest_position = (
        Many(center_positions_with_labels.keys())
        .map(list)
        .order_values_by(key=lambda _p: distance_function(position, _p))
        .unwrap_as_pipeline()
        .map(lambda _positions: list(_positions)[0])
        .unwrap()
    )

    return center_positions_with_labels[_closest_position]


def iter_generate(
    size: Size2,
    distance_function: DistanceFunction2,
    group_center_generator: Position2Generator,
) -> Iterable[VoronoiLevel2]:
    _level = Level2(size, DEFAULT_TILE)
    yield _level

    _labeled_group_centers = {
        _group_center: _group_num + 1
        for _group_num, _group_center in enumerate(group_center_generator())
    }

    for _position, _tile in _labeled_group_centers.items():
        _level = _level.set_at(_position, _tile)
        yield _level

    for _position in iter_positions(size):
        if _position in _labeled_group_centers:
            continue
        _closest_tile = get_closes_tile(
            _position,
            _labeled_group_centers,
            distance_function,
        )

        _level = _level.set_at(_position, _closest_tile)
        yield _level


def complete(levels: Iterable[VoronoiLevel2]) -> VoronoiLevel2:
    return list(levels)[-1]
