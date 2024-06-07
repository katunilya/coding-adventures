from rich.table import Table

from adventure.voronoi import VoronoiMap
from adventure.wfc_sudoku import (
    _SIZE,
    SudokuCell,
    SudokuGrid,
    get_value,
)


def sudoku_grid_to_rich_table(grid: SudokuGrid) -> Table:
    _table = Table(
        title="SUDOKU",
        show_header=False,
        show_lines=True,
    )

    def _cell_to_rich_text(cell: SudokuCell) -> str:
        if len(cell) == 1:
            return f"[green bold]{get_value(cell)}[/]"
        else:
            return f"[red]{len(cell)}[/]"

    for _row in range(_SIZE):
        _table.add_row(*[_cell_to_rich_text(_cell) for _cell in grid[_row]])

    return _table


def colored_voronoi_map(_map: VoronoiMap, count: int) -> str:
    _result = ""
    for _row in _map:
        for _tile in _row:
            _color_num = 0 if _tile == -1 else _tile + 15

            _result += f"[on color({_color_num})]  [/]"
        _result += "\n"

    return _result
