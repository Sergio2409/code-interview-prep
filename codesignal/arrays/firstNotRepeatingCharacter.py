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
Name: firstNotRepeatingCharacter

Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in
it. If there is no such character, return '_'.

"""


def solution(a):
    cache = {}
    res = []
    removed ={}
    for el in a:
        if cache.get(el, False):
            cache.pop(el)
            res.remove(el)
            removed[el] = el
        else:
            if removed.get(el, False):
                continue
            cache[el] = el
            res.append(el)
    return res[0] if len(res) > 0 else '_'
