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
Module description goes here

"""

def utopianTree(n):
    # Write your code here
    tree_heigth = 0
    duplicate = False
    for period in range(0, n+1):
        if not duplicate:
            tree_heigth += 1
            duplicate = True
        else:
            tree_heigth *= 2
            duplicate = False
    return tree_heigth


if __name__ == '__main__':
    print(utopianTree(0) == 1)
    print(utopianTree(1) == 2)
    print(utopianTree(4) == 7)
    print(utopianTree(3) == 6)
    print(utopianTree(5) == 14)