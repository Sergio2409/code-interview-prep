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
Name: firstDuplicate

Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which
the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the
number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there
are no such elements, return -1.

"""


def solution(a):
    cache = {}
    for el in a:
        if not cache.get(el, False):
            cache[el] = el
        else:
            return el
    return -1
