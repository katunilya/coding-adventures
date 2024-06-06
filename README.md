# Coding Adventures

Repository with some simple code tasks solved. Each adventure is a single python
module, in some cases it provides some interaction via CLI `adventure`.

## Adventures

- [Wave Function Collapse Sudoku Solution](/adventure/wfc_sudoku.py)

  Simple implementation of Wave Function Collapse algorithm for solving sudoku
  puzzle. Can be used via CLI with:

  ```sh
  adventure wfc-sudoku
  ```

  Can output individual steps of solution.

  > Sometimes fails due to random choices that lead to cases with impossible
  > solutions

  Example:

  ![WFC Sudoku Example](./imgs/wfc-sudoku.gif)
