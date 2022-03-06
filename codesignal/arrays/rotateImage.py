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
 Name: rotateImage

 Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an
 interview.

 You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

"""


def solution(a):
    n = len(a)
    for i in range(n//2):
        for j in range(i, n - 1 - i):
            tmp = a[i][j]
            # top_left
            a[i][j] = a[n - 1 - j][i]
            # bot_left
            a[n - 1 - j][i] = a[n - 1 - i][n - 1 -j]
            # bot_rigth
            a[n - 1 - i][n - 1 -j] = a[j][n - 1 - i]
            # top_rigth
            a[j][n - 1 - i] = tmp
    return a
