#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# Mail: sergiovaldes2409@gmail.com
#
# All rights reserved.
#
#
splited = lambda x: x.split()

def designerPdfViewer(h, word):
    # Write your code here
    letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    letters = splited(letters)
    heights = {}
    b = len(word)
    a = 1
    for num, value in enumerate(h):
        heights[letters[num]] = value
    for char in word:
        if heights[char] > a:
            a = heights[char]
    return a * b


def gen_data1():
    h = '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'
    h = [int(el) for el in h.split()]
    word = 'abc'
    res = 9
    return h, word, res


def gen_data2():
    h = '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7'
    h = [int(el) for el in h.split()]
    word = 'zaba'
    res = 28
    return h, word, res


if __name__ == '__main__':
    print(designerPdfViewer(gen_data1()[0], gen_data1()[1]) == gen_data1()[2])
    print(designerPdfViewer(gen_data2()[0], gen_data2()[1]) == gen_data2()[2])
