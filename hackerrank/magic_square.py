#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# Mail: sergiovaldes2409@gmail.com
#
# All rights reserved.
#
#
def gen_corner_pos():
    return list(zip([0, 0, 2, 2], [0, 2, 0, 2]))


def gen_iner_corner_pos():
    return list(zip([0, 1, 1, 2], [1, 0, 2, 1], [True, False, False, True]))


def gen_matrix(rows, cols, value=0):
    return [[value]*cols for _ in range(rows)]


def corner_matrix(values):
    matrix = gen_matrix(3, 3)
    for pos, point in enumerate(gen_corner_pos()):
        matrix[point[0]][point[1]] = values[pos]
    return matrix


def corners_matrices():
    list_values = [
        [2, 4, 6, 8],
        [2, 6, 4, 8],
        [4, 2, 8, 6],
        [4, 8, 2, 6],
        [6, 2, 8, 4],
        [6, 8, 2, 4],
        [8, 4, 6, 2],
        [8, 6, 4, 2],
    ]
    return list(map(corner_matrix, list_values))


def check_inn_corner(matrix, x, y, is_row):
    amount = 0
    if is_row:
        resultant = 15 - (matrix[x][y-1] + matrix[x][y+1])

        if matrix[x][y] != resultant:
            amount = abs(matrix[x][y]-resultant)
            matrix[x][y] = resultant
            return matrix, amount
    else:
        resultant = 15 - (matrix[x - 1][y] + matrix[x + 1][y])
        if matrix[x][y] != resultant:
            amount = abs(matrix[x][y] - resultant)
            matrix[x][y] = resultant
            return matrix, amount
    return matrix, amount


def find_corner(from_matrix):
    min_amount = 99999999999999
    corner = None
    for matrix in corners_matrices():
        amount = 0
        for x, y in gen_corner_pos():
            amount += abs(matrix[x][y] - from_matrix[x][y])
        if amount < min_amount:
            min_amount = amount
            corner = matrix
    print(from_matrix, corner, min_amount)
    return corner, min_amount


def merge_matrix_with_corner(m, corner):
    amount = 0
    for x, y in gen_corner_pos():
        if m[x][y] != corner[x][y]:
            amount += abs(m[x][y] - corner[x][y])
            m[x][y] = corner[x][y]
    return m, amount


def formingMagicSquare(initial):
    # Write your code here
    min_amount = 99999
    f_am = 0
    if initial[1][1] != 5:
        f_am += abs(initial[1][1] - 5)
    for corner in corners_matrices():
        m = [el.copy() for el in initial]
        m, amount = merge_matrix_with_corner(m, corner)
        print(f's:{initial} corner:{corner}', amount)
        amount2 = 0
        for x, y, is_row in gen_iner_corner_pos():
            m, aux = check_inn_corner(m, x, y, is_row)
            amount2 += aux
        amount += amount2 + f_am
        if amount < min_amount:
            min_amount = amount
    return min_amount


if __name__ == '__main__':
    new_masdasd_asdasd = [[2, 9, 8], [4, 2, 7], [5, 6, 7]] #This example must return 21
    print(formingMagicSquare(new_masdasd_asdasd))


