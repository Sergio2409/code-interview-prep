#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# Mail: sergiovaldes2409@gmail.com
#
# All rights reserved.
#
#
"""
Name: sudoku2

 Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column,
 each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one
 time.

 Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to
 the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

"""


def solution(grid):
    rows = grid
    cols = zip(*grid)
    subs = []

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            subs.append([grid[r][c] for r in range(i, i+3) for c in range(j, j+3)])

    def is_valid(arr):
        nums = [el for el in arr if str.isdigit(el)]
        return len(nums) == len(set(nums))

    return all([
        all(map(is_valid, rows)),
        all(map(is_valid, cols)),
        all(map(is_valid, subs))
    ])


if __name__ == '__main__':
    grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
            ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
            ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
            ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
            ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
    print(solution(grid) == True)
