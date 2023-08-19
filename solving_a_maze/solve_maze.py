from __future__ import annotations

import sys
from typing import List, Tuple

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

WALL = "*"
STARTING_POINT = "o"
EXIT_POINT = "x"
VISITED = "v"

RIGHT = 1
FORWARD = 0
LEFT = 3
BACKWARD = 2


def load_from_file(filename: str) -> List[List[str]]:
    maze = []
    with open(filename, "r", encoding="utf-8") as reader:
        while line := reader.readline():
            row = [cell_value for cell_value in line.strip()]
            for pos_x, cell_value in enumerate(row):
                pos_y = len(maze)
                if cell_value == STARTING_POINT:
                    starting_point = (pos_x, pos_y)
                elif cell_value == EXIT_POINT:
                    end_point = (pos_x, pos_y)
            maze.append(row)
    return maze, starting_point, end_point


def next_move(
    maze: List[List[str]], current_position: Tuple[int, int], heading: int
) -> Tuple[Tuple[int, int], int]:
    step = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for direction in (RIGHT, FORWARD, LEFT, BACKWARD):
        new_heading = (heading + direction) % len(step)
        new_position = (
            current_position[0] + step[new_heading][0],
            current_position[1] + step[new_heading][1],
        )
        cell_value = maze[new_position[1]][new_position[0]]
        if cell_value != WALL and cell_value != VISITED:
            return new_position, new_heading


def solve(
    maze: List[List[str]], current_position: Tuple[int, int], end_point: Tuple[int, int]
) -> List[Tuple[int, int]]:
    heading = NORTH
    moves = [current_position]
    while current_position != end_point:
        maze[current_position[1]][current_position[0]] = VISITED
        current_position, heading = next_move(maze, current_position, heading)
        moves.append(current_position)
    return moves


filename = sys.argv[1]
print(solve(*load_from_file(filename)))
