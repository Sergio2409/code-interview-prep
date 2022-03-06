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


def pickingNumbers(a):
    # Write your code here
    count = 0
    a.sort()
    for i in range(len(a)-1):
        init = a[i]
        aux_conter = 1
        for j in range(i+1, len(a)):
            if a[j] <= init + 1:
                aux_conter += 1
            else:
                if aux_conter > count:
                    count = aux_conter
                break
        if aux_conter > count:
            count = aux_conter
    return count

if __name__ == '__main__':
    a = [1,1,2,2,4,4,5,5,5]
    print(pickingNumbers(a))