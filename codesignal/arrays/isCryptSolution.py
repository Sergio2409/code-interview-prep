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
 A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such
 that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

 You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits,
 solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3],
 which should be interpreted as the word1 + word2 = word3 cryptarithm.

 If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in
 solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it
 does not become a valid arithmetic solution, the answer is false.

 Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

"""


def solution(crypt, sol):
    cache = {}
    for el in sol:
        cache[el[0]] = el[1]

    def decrypt(phrase):
        return ''.join([cache[c] for c in phrase])

    def has_not_leading_zeros(phrase):
        if len(phrase) == 1:
            return True
        return not phrase.startswith('0')

    def is_valid_exp(phrases):
        try:
            res = eval(f'{phrases[0]} + {phrases[1]} == {phrases[2]}')
            return res
        except SyntaxError as e:
            return False

    decrypted = [decrypt(p) for p in crypt]
    return all(map(has_not_leading_zeros, decrypted)) and is_valid_exp(decrypted)


if __name__ == '__main__':
    sol1 = [['O', '0'],
           ['M', '1'],
           ['Y', '2'],
           ['E', '5'],
           ['N', '6'],
           ['D', '7'],
           ['R', '8'],
           ['S', '9']]

    crypt1 = ["SEND", "MORE", "MONEY"]
    print(solution(crypt1, sol1) == True)

    sol2 = [['A', '0']]

    crypt2 = ["AA", "AA", "AA"]
    print(solution(crypt2, sol2) == False)