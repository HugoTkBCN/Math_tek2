#!/usr/bin/python3
##
## EPITECH PROJECT, 2020
## yams
## File description:
## yams
##

import locale

def print_usage():
    print("USAGE")
    print("    ./201yams d1 d2 d3 d4 d5 c\n")
    print("DESCRIPTION")
    print("    d1    value of the first die (0 if not thrown)")
    print("    d2    value of the second die (0 if not thrown)")
    print("    d3    value of the third die (0 if not thrown)")
    print("    d4    value of the fourth die (0 if not thrown)")
    print("    d5    value of the fifth die (0 if not thrown)")
    print("    c     expected combination")

def display(_type, count, nb, nb2 = None) :
    if (nb2) :
        print("Chances to get a " + str(nb) + " full of " + str(nb2) + ": ", end="")
        print ("%.2f" % count + "%")
    else :
        count = float(count)
        print("Chances to get a " + nb + " " + _type + ": ", end="")
        print ("%.2f" % count + "%")

def listToDict(lst):
    op = { i : lst[i] for i in range(0, len(lst) ) }
    return (op)

def number_format(num, places=0):
    return (locale.format("%.*f", (places, num), True))
