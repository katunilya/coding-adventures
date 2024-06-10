import random
from pathlib import Path
from typing import Annotated, Optional

import typer
from tibia import Compose, Pipeline

from adventure.cli.common import add_command
from adventure.cli.level_generation.output import voronoi as voronoi_output
from adventure.level_generation.distance import (
    DistanceFunction2Kind,
    get_distance_function2,
)
from adventure.level_generation.generators import voronoi
from adventure.level_generation.generators.position import (
    Position2GeneratorKind,
    get_position2_generator,
)
from adventure.level_generation.utils import get_size2_area


def generate_voronoi(
    rows: Annotated[int, typer.Argument(min=1)],
    cols: Annotated[int, typer.Argument(min=1)],
    group_count: Annotated[int, typer.Argument(min=1)],
    group_generator: Annotated[
        Position2GeneratorKind, typer.Option()
    ] = Position2GeneratorKind.NAIVE,
    distance_function: Annotated[
        DistanceFunction2Kind, typer.Option()
    ] = DistanceFunction2Kind.EULER,
    min_distance: Annotated[Optional[float], typer.Option()] = None,
    fuzz_radius: Annotated[Optional[float], typer.Option()] = None,
    live: Annotated[bool, typer.Option()] = True,
    animation_time: Annotated[float, typer.Option()] = 10.0,
    save_path: Annotated[Optional[Path], typer.Option()] = None,
    image_scale: Annotated[int, typer.Option(min=1)] = 10,
    seed: Annotated[Optional[int], typer.Option()] = None,
):
    if seed is not None:
        random.seed(seed)
    _size = (rows, cols)
    _distance_function = get_distance_function2(distance_function)
    _group_generator = get_position2_generator(
        group_generator,
        count=group_count,
        size=_size,
        min_distance=min_distance,
        distance_function=_distance_function,
        fuzz_radius=fuzz_radius,
    )

    _generator = voronoi.iter_generate(
        _size,
        _distance_function,
        _group_generator,
    )

    if not live:
        _ = (
            Pipeline(_generator)
            .map(voronoi.complete)
            .map(voronoi_output.rich_show)
            .map(voronoi_output.maybe_image_save(save_path, image_scale))
            .unwrap()
        )

    else:
        _ = (
            Pipeline(_generator)
            .map(voronoi_output.rich_show_live(animation_time / get_size2_area(_size)))
            .map(
                voronoi_output.maybe_image_save_live(
                    save_path,
                    animation_time,
                    image_scale,
                )
            )
            .map(voronoi.complete)
            .unwrap()
        )


def generate_voronoi_all(
    rows: Annotated[int, typer.Argument(min=1)],
    cols: Annotated[int, typer.Argument(min=1)],
    group_count: Annotated[int, typer.Argument(min=1)],
    save_path: Annotated[Path, typer.Argument(file_okay=False, dir_okay=True)],
    min_distance: Annotated[float, typer.Option()],
    fuzz_radius: Annotated[float, typer.Option()],
    image_scale: Annotated[int, typer.Option(min=1)] = 10,
    seed: Annotated[Optional[int], typer.Option()] = None,
):
    if seed is not None:
        random.seed(seed)
    _size = (rows, cols)

    for _distance_function_kind in DistanceFunction2Kind:
        _distance_function = get_distance_function2(_distance_function_kind)
        for _group_generator_kind in Position2GeneratorKind:
            _group_generator = get_position2_generator(
                _group_generator_kind,
                count=group_count,
                size=_size,
                min_distance=min_distance,
                distance_function=_distance_function,
                fuzz_radius=fuzz_radius,
            )

            _generator = voronoi.iter_generate(
                _size,
                _distance_function,
                _group_generator,
            )

            _file_name = str(
                "voronoi-"
                + _distance_function_kind.value
                + "-"
                + _group_generator_kind.value
                + ("" if seed is None else f"-{seed}")
                + ".png"
            )
            _save_path = save_path / _file_name

            _ = (
                Pipeline(_generator)
                .map(voronoi.complete)
                .map(voronoi_output.rich_show)
                .map(voronoi_output.maybe_image_save(_save_path, image_scale))
                .unwrap()
            )


def add(app: typer.Typer):
    return (
        Pipeline(app)
        .map(
            add_command(
                generate_voronoi,
                name="voronoi",
                help="Voronoi Diagram generation",
            )
        )
        .map(
            add_command(
                generate_voronoi_all,
                name="voronoi-all",
                help="generate all combinations of generators for Voronoi Diagrams",
            )
        )
        .unwrap()
    )
