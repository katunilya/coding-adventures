import random
import string
from collections import defaultdict
from copy import deepcopy
from pathlib import Path
from typing import Final, Iterable, Literal

type SudokuCellValue = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]
type SudokuCell = set[SudokuCellValue]
type SudokuGrid = list[list[SudokuCell]]
type ValidPositionValue = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
type Position = tuple[ValidPositionValue, ValidPositionValue]

_SIZE: Final = 9
_ALL_OPTIONS = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def iter_positions() -> Iterable[Position]:
    for _row in range(_SIZE):
        for _col in range(_SIZE):
            yield _row, _col


def get_cell(grid: SudokuGrid, position: Position) -> SudokuCell:
    _row, _col = position
    return grid[_row][_col]


def set_cell(grid: SudokuGrid, position: Position, cell: SudokuCell) -> SudokuGrid:
    _row, _col = position
    grid[_row][_col] = cell
    return grid


def get_value(cell: SudokuCell) -> SudokuCellValue:
    if len(cell) != 1:
        raise ValueError("cell is not collapsed")

    return list(cell)[0]


def get_min_entropy_cell_position(grid: SudokuGrid) -> Position:
    _min_entropy = 10
    _min_entropy_cell_positions = set[Position]()

    for _position in iter_positions():
        _cell = get_cell(grid, _position)
        _entropy = len(_cell)

        if _entropy == 1:
            continue

        if _entropy <= _min_entropy:
            if _entropy < _min_entropy:
                _min_entropy_cell_positions.clear()

            _min_entropy_cell_positions.add(_position)
            _min_entropy = _entropy

    if len(_min_entropy_cell_positions) == 0:
        raise ValueError("all cells are collapsed")

    return random.choice(list(_min_entropy_cell_positions))


def collapse(grid: SudokuGrid, position: Position) -> SudokuGrid:
    return set_cell(grid, position, {random.choice(list(get_cell(grid, position)))})


def get_allowed_zone_options(grid: SudokuGrid, position: Position) -> SudokuCell:
    _picked_options: SudokuCell = set()

    _row, _col = position
    _row_start, _col_start = (_row // 3) * 3, (_col // 3) * 3

    for _r in range(_row_start, _row_start + 3):
        for _c in range(_col_start, _col_start + 3):
            if (_r, _c) == position:
                continue

            _cell = get_cell(grid, (_r, _c))

            if len(_cell) == 1:
                _picked_options.add(get_value(_cell))

    return _ALL_OPTIONS.difference(_picked_options)


def get_allowed_row_options(grid: SudokuGrid, position: Position) -> SudokuCell:
    _picked_options: SudokuCell = set()
    _row, _col = position

    for _r in range(_SIZE):
        if _row == _r:
            continue

        _cell = get_cell(grid, (_r, _col))
        if len(_cell) == 1:
            _picked_options.add(get_value(_cell))

    return _ALL_OPTIONS.difference(_picked_options)


def get_allowed_col_options(grid: SudokuGrid, position: Position) -> SudokuCell:
    _picked_options: SudokuCell = set()
    _row, _col = position

    for _c in range(_SIZE):
        if _col == _c:
            continue

        _cell = get_cell(grid, (_row, _c))
        if len(_cell) == 1:
            _picked_options.add(get_value(_cell))

    return _ALL_OPTIONS.difference(_picked_options)


def get_allowed_options(grid: SudokuGrid, position: Position) -> SudokuCell:
    _col_options = get_allowed_col_options(grid, position)
    _row_options = get_allowed_row_options(grid, position)
    _zone_options = get_allowed_zone_options(grid, position)

    _allowed = _col_options & _row_options & _zone_options

    if len(_allowed) == 0:
        raise ValueError("cannot leave 0 allowed options")

    return _allowed


def remove_invalid_options(grid: SudokuGrid) -> tuple[SudokuGrid, bool]:
    _new_collapses = False
    for _position in iter_positions():
        _cell = get_cell(grid, _position)
        if len(_cell) == 1:
            continue

        _allowed = get_allowed_options(grid, _position)

        if _cell != _allowed:
            grid = set_cell(grid, _position, _allowed)
            if len(_allowed) == 1:
                _new_collapses = True

    return grid, _new_collapses


def propagate(grid: SudokuGrid) -> SudokuGrid:
    while True:
        grid, _new_collapses = remove_invalid_options(grid)

        if not _new_collapses:
            break

    return grid


def is_collapsed(grid: SudokuGrid) -> bool:
    for _position in iter_positions():
        _cell = get_cell(grid, _position)
        if len(_cell) > 1:
            return False

    return True


def is_row_valid(grid: SudokuGrid, row: ValidPositionValue) -> bool:
    _collapsed_value_counter: dict[SudokuCellValue, int] = defaultdict(int)

    for _col in range(_SIZE):
        _position = row, _col
        _cell = get_cell(grid, _position)
        if len(_cell) == 1:
            _collapsed_value_counter[get_value(_cell)] += 1

    return set(_collapsed_value_counter.keys()).issubset(_ALL_OPTIONS) and not any(
        [_count > 1 for _count in _collapsed_value_counter.values()]
    )


def is_rows_valid(grid: SudokuGrid) -> bool:
    return all([is_row_valid(grid, _row) for _row in range(_SIZE)])


def is_col_valid(grid: SudokuGrid, col: ValidPositionValue) -> bool:
    _collapsed_value_counter: dict[SudokuCellValue, int] = defaultdict(int)

    for _row in range(_SIZE):
        _position = _row, col
        _cell = get_cell(grid, _position)
        if len(_cell) == 1:
            _collapsed_value_counter[get_value(_cell)] += 1

    return set(_collapsed_value_counter.keys()).issubset(_ALL_OPTIONS) and not any(
        [_count > 1 for _count in _collapsed_value_counter.values()]
    )


def is_cols_valid(grid: SudokuGrid) -> bool:
    return all([is_row_valid(grid, _col) for _col in range(_SIZE)])


def is_zone_valid(
    grid: SudokuGrid, row: Literal[0, 3, 6], col: Literal[0, 3, 6]
) -> bool:
    _collapsed_value_counter: dict[SudokuCellValue, int] = defaultdict(int)

    for _row in range(row, row + 3):
        for _col in range(col, col + 3):
            _position = _row, _col
            _cell = get_cell(grid, _position)
            if len(_cell) == 1:
                _collapsed_value_counter[get_value(_cell)] += 1

    return set(_collapsed_value_counter.keys()).issubset(_ALL_OPTIONS) and not any(
        [_count > 1 for _count in _collapsed_value_counter.values()]
    )


def is_zones_valid(grid: SudokuGrid) -> bool:
    return all(
        [
            all([is_zone_valid(grid, _row, _col) for _col in [0, 3, 6]])
            for _row in [0, 3, 6]
        ]
    )


def is_valid(grid: SudokuGrid) -> bool:
    return is_rows_valid(grid) and is_cols_valid(grid) and is_zones_valid(grid)


def iter_solution(grid: SudokuGrid) -> Iterable[SudokuGrid]:
    if not is_valid(grid):
        raise ValueError("cannot solve invalid sudoku grid")

    while True:
        _position = get_min_entropy_cell_position(grid)
        grid = collapse(grid, _position)
        grid = propagate(grid)

        if not is_valid(grid):
            raise ValueError("cannot solve invalid sudoku grid")

        yield grid

        if is_collapsed(grid):
            return


def solve(grid: SudokuGrid) -> Iterable[SudokuGrid]:
    return list(iter_solution(grid))[-1]


def get_empty_sudoku_grid() -> SudokuGrid:
    _grid: SudokuGrid = []

    for _row in range(_SIZE):
        _grid.append([])
        for _ in range(_SIZE):
            _grid[_row].append(deepcopy(_ALL_OPTIONS))

    return _grid


def get_sudoku_grid_from_file(path: Path) -> SudokuGrid:
    _grid = get_empty_sudoku_grid()

    _raw = [_line.split(",") for _line in path.read_text().split("\n")]

    for _row, _line in enumerate(_raw):
        for _col, _char in enumerate(_line):
            _position = _row, _col
            try:
                _grid = set_cell(
                    _grid, _position, {int(_char.strip(string.ascii_letters))}
                )
            except Exception:
                ...

    return _grid
