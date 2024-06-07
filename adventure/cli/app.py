import random
import time
from enum import Enum
from pathlib import Path
from typing import Annotated, Optional

import rich
import typer
from rich.live import Live
from tibia import Compose, Pipeline, passing

from adventure.cli.output.console import colored_voronoi_map, sudoku_grid_to_rich_table
from adventure.voronoi import (
    chebyshev_distance,
    euler_distance,
    fuzzy_grid_distribution,
    generate,
    iter_generate,
    manhattan_distance,
    min_distance_random_distribution,
    random_distribution,
)
from adventure.wfc_sudoku import (
    get_empty_sudoku_grid,
    get_sudoku_grid_from_file,
    iter_solution,
    solve,
)

app = typer.Typer(
    name="adventure",
    add_completion=False,
)


@app.command(name="wfc-sudoku")
def wave_function_collapse_sudoku(
    path: Annotated[
        Optional[Path],
        typer.Option(
            file_okay=True,
            dir_okay=False,
        ),
    ] = None,
    overtime: Annotated[bool, typer.Option()] = True,
    step_by_step: Annotated[bool, typer.Option()] = False,
    frame_time: Annotated[float, typer.Option()] = 0.5,
    seed: Annotated[Optional[int], typer.Option()] = None,
):
    if seed is not None:
        random.seed(seed)

    _grid = get_empty_sudoku_grid() if path is None else get_sudoku_grid_from_file(path)

    if overtime:
        with Live(sudoku_grid_to_rich_table(_grid)) as _live:
            for _next_grid in iter_solution(_grid):
                _live.update(sudoku_grid_to_rich_table(_next_grid))
                time.sleep(frame_time)

        return

    if step_by_step:
        with Live(sudoku_grid_to_rich_table(_grid)) as _live:
            for _next_grid in iter_solution(_grid):
                input()
                _live.update(sudoku_grid_to_rich_table(_next_grid))

        return

    _ = (
        Pipeline(_grid)
        .map(solve)
        .map(passing(Compose(sudoku_grid_to_rich_table).then(rich.print)))
        .unwrap()
    )


class DistanceFunction(str, Enum):
    EULER = "euler"
    MANHATTAN = "manhattan"
    CHEBYSHEV = "chebyshev"


class DistributionFunction(str, Enum):
    RANDOM = "random"
    MIN_DISTANCE = "min-distance"
    FUZZY_GRID = "fuzzy-grid"


@app.command(name="voronoi")
def voronoi(
    rows: Annotated[int, typer.Argument(min=1)],
    cols: Annotated[int, typer.Argument(min=1)],
    group_count: Annotated[int, typer.Argument(min=1)],
    distance_function: Annotated[
        DistanceFunction, typer.Option()
    ] = DistanceFunction.EULER,
    distribution_function: Annotated[
        DistributionFunction, typer.Option()
    ] = DistributionFunction.RANDOM,
    fuzz_radius: Annotated[Optional[float], typer.Option()] = None,
    min_distance: Annotated[Optional[float], typer.Option()] = None,
    overtime: Annotated[bool, typer.Option()] = False,
    frame_time: Annotated[float, typer.Option()] = 0.5,
    seed: Annotated[Optional[int], typer.Option()] = None,
):
    if seed is not None:
        random.seed(seed)
    match distance_function:
        case DistanceFunction.EULER:
            _distance_function = euler_distance
        case DistanceFunction.MANHATTAN:
            _distance_function = manhattan_distance
        case _:
            _distance_function = chebyshev_distance

    match distribution_function:
        case DistributionFunction.RANDOM:
            _distribution_function = random_distribution
        case DistributionFunction.FUZZY_GRID:
            if fuzz_radius is None:
                raise ValueError("fuzz-radius is required for fuzzy-grid distribution")
            _distribution_function = fuzzy_grid_distribution(fuzz_radius)

        case _:
            if min_distance is None:
                raise ValueError(
                    "min-distance is required for min-distance distribution"
                )

            _distribution_function = min_distance_random_distribution(
                min_distance,
                _distance_function,
            )

    if overtime:
        with Live("") as _live:
            for _next_grid in iter_generate(
                (rows, cols),
                group_count,
                _distance_function,
                _distribution_function,
            ):
                _live.update(colored_voronoi_map(_next_grid, group_count))
                time.sleep(frame_time)

        return

    _ = (
        Pipeline(
            generate(
                (rows, cols),
                group_count,
                _distance_function,
                _distribution_function,
            )
        )
        .map(
            passing(
                Compose(lambda _map: colored_voronoi_map(_map, group_count)).then(
                    rich.print
                )
            )
        )
        .unwrap()
    )


@app.command(name="ping")
def ping():
    rich.print("PONG!")
