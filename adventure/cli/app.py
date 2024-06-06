import random
import time
from pathlib import Path
from typing import Annotated, Optional

import rich
import typer
from rich.live import Live

from adventure.cli.output.console import sudoku_grid_to_rich_table
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
    frame_time: Annotated[float, typer.Option()] = 0.5,
    seed: Annotated[Optional[int], typer.Option()] = None,
):
    if seed is not None:
        random.seed(seed)

    _grid = get_empty_sudoku_grid() if path is None else get_sudoku_grid_from_file(path)

    if not overtime:
        sudoku_grid_to_rich_table(solve(_grid))
        return

    with Live(sudoku_grid_to_rich_table(_grid)) as _live:
        for _next_grid in iter_solution(_grid):
            _live.update(sudoku_grid_to_rich_table(_next_grid))
            time.sleep(frame_time)


@app.command(name="ping")
def ping():
    rich.print("PONG!")
