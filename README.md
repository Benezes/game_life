__John Conway's Game of Life.__

It is a cellular automaton devised by the mathematician John Horton Conway. 
The game is a zero-player game, meaning that its evolution is determined by its initial state, 
without any further input. 
You interact with the Game of Life by creating an initial configuration and observing how it evolves.



__Rules of the Game__

The universe of the Game of Life is a two-dimensional orthogonal grid of square cells,
each of which is in one of two possible states: alive or dead (or populated and unpopulated). 
Every cell interacts with its eight neighbors, which are the cells that are horizontally, 
vertically, or diagonally adjacent.

At each step in time, the following transitions occur:

    1 - Any live cell with fewer than two live neighbors dies (underpopulation).

    2- Any live cell with two or three live neighbors lives on to the next generation.

    3 - Any live cell with more than three live neighbors dies (overcrowding).

    4 - Any dead cell with exactly three live neighbors becomes a live cell (reproduction).



__To run__

Execute requirements
```sh
python -m pip install -r requirements.txt
```

Run code
```sh
python app.py
```