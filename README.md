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

  ![WFC Sudoku Example](https://raw.githubusercontent.com/katunilya/coding-adventures/main/imgs/wfc-sudoku.gif)

- [Voronoi](/adventure/voronoi.py)

  Very simple and not optimal in terms of complexity ($O$-notation) implementation of algorithm
  for generating Voronoi Diagrams.

  Provides 3 distance functions:

  - Euler

    Default distance function, widely known by everyone.

    $$
    \sqrt{(x_1 - x_2) ^ 2 + (y_1 - y_2) ^ 2}
    $$

  - Manhattan

    Also known as "taxicab" distance, calculated as length of vertical and
    horizontal moves from one position to another.

    $$
    |x_1 - x_2| + |y_1 - y_2|
    $$

  - Chebyshev

    Distance function calculated as max difference between $x$ and $y$ of
    positions.

    $$
    \max (|x_1 - x_2|, |y_1 - y_2|)
    $$

  For generating random centers of groups I also provide 3 different approaches:

  | Approach            | Description                                                                                                                                 |
  | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
  | Random              | Generates random $x$ & $y$ for each group center; Guarantees generation of exact number of groups                                           |
  | Min Distance Random | Generates random $x$ & $y$ for each group center; Guarantees generation of exact number of groups and minimal distance between group center |
  | Fuzzy Grid          | Builds a grid of evenly distributed center and than based on fuzz radius randomly moves them around initial position                        |

  ![Voronoi Diagrams](https://raw.githubusercontent.com/katunilya/coding-adventures/main/imgs/voronoi.png)
