#!/usr/bin/python3
##
## EPITECH PROJECT, 2020
## yams
## File description:
## yams
##

from collections import Counter

def facto(n) :
    if n == 0 :
        return (1)
    else :
        return (n * facto(n - 1))

def comb(a, b) :
    return (facto(a) / (facto(b) * facto(a - b)))

def bin(a, b) :
    return (comb(a, b) * pow(1/6, b) * pow(5/6, a-b))

def calc(_type, n) :
    result = 0
    if n >= _type :
        return (1)
    else:
        i = _type - n
        while i <= (5 - n) :
            result += bin(5 - n, i)
            i += 1
    return (result)

def get_nbr_occ(num, dices):
    i = 0
    res = 0
    while (i < 5):
        if (int(dices[i]) == num):
            res += 1
        i += 1
    if (res > 1):
        res = 1
    return (res)

def yams(n) :
    return (calc(5, n))

def four(n) :
    return (calc(4, n))

def brolan(n) :
    return (calc(3, n))

def pair(n) :
    return (calc(2, n))

def full(three, pair) :
    return (comb(5 - three - pair, 3 - three) * pow(1/6, 5 - three - pair))

def straight(nb, dices) :
    if (int(nb) == 6):
        nbr_occ = get_nbr_occ(2, dices) + get_nbr_occ(3, dices) + get_nbr_occ(4, dices) + get_nbr_occ(5, dices) + get_nbr_occ(6, dices)
    else:
        nbr_occ = get_nbr_occ(1, dices) + get_nbr_occ(2, dices) + get_nbr_occ(3, dices) + get_nbr_occ(4, dices) + get_nbr_occ(5, dices)
    if nbr_occ == 5:
        return (1)
    else:
        return (facto(5 - nbr_occ) / pow(6, (5 - nbr_occ)))