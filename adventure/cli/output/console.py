from rich.table import Table

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
