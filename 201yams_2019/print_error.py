#!/usr/bin/python3
##
## EPITECH PROJECT, 2020
## 201yams
## File description:
## yams
##

def print_error(str) :
    print ("Error: " + str)
    exit(84)

def check_error(numbers, _type) :
    _list = ["pair", "three", "four", "full", "straight", "yams"]
    _bool = False
    if numbers[0] == 0 :
        for number in numbers :
            if number != 0:
                print_error("Bad first roll of dice, you can't have a value asigned to a dice")
    other = 0
    zero = 0
    for number in numbers :
        if number.isnumeric() == 0 or int(number) > 6 or int(number) < 0 :
            print_error("Bad combinaison")
        if int(number) == 0:
            if other == 1:
                print_error("Bad combinaison")
            else:
                zero = 1
        else:
            if zero == 1:
                print_error("Bad combinaison")
            other = 1
    for l in _list :
        if l == _type[0] :
            _bool = True
    if _bool == False :
        print_error("Bad combinaison")
    elif len(_type) < 2:
        print_error("Synthax. Run with -h")
    elif _type[0] == "straight" and (int(_type[1]) != 5 and int(_type[1]) != 6) :
        print_error("Straight can only be of 5 or 6")
    elif _type[1].isnumeric() == 0 or int(_type[1]) > 6 or int(_type[1]) <= 0 :
        print_error("Bad number to find 0 < nbr <= 6")
