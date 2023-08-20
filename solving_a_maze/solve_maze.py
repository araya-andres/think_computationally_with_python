from __future__ import annotations

import sys
from typing import List, Optional, Tuple
from enum import IntEnum, StrEnum


class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Move(IntEnum):
    FORWARD = 0
    RIGHT = 1
    BACKWARD = 2
    LEFT = 3


class Cell(StrEnum):
    EMPTY = " "
    EXIT_POINT = "x"
    STARTING_POINT = "o"
    VISITED = "v"
    WALL = "*"


STEP = ((0, -1), (1, 0), (0, 1), (-1, 0))


def load_from_file(filename: str) -> List[List[str]]:
    maze = []
    with open(filename, "r", encoding="utf-8") as reader:
        while line := reader.readline():
            row = list(line.strip())
            for pos_x, cell in enumerate(row):
                if cell == Cell.STARTING_POINT:
                    starting_point = (pos_x, len(maze))
            maze.append(row)
    return maze, starting_point


def get_cell(maze: List[List[str]], position: Tuple[int, int]) -> Cell:
    return Cell(maze[position[1]][position[0]])


def set_cell(maze: List[List[str]], position: Tuple[int, int], cell_value: Cell):
    maze[position[1]][position[0]] = cell_value.value


def find_path(
    maze: List[List[str]],
    current_position: Tuple[int, int],
    heading: Direction,
    path: List[Tuple[int, int]],
) -> Optional[List[Tuple[int, int]]]:
    path.append(current_position)
    set_cell(maze, current_position, Cell.VISITED)
    for move in (Move.RIGHT, Move.FORWARD, Move.LEFT, Move.BACKWARD):
        new_heading = Direction((heading + move) % len(STEP))
        new_position = (
            current_position[0] + STEP[new_heading][0],
            current_position[1] + STEP[new_heading][1],
        )
        cell = get_cell(maze, new_position)
        if cell == Cell.EXIT_POINT:
            path.append(new_position)
            return path
        if cell == Cell.EMPTY:
            if path_to_exit := find_path(maze, new_position, new_heading, list(path)):
                return path_to_exit
    return None


print(find_path(*load_from_file(sys.argv[1]), Direction.NORTH, []))
