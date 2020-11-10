#!/usr/bin/python3

def prob(x, y, a, b):
    return ((a - x) * (b - y)) / ((5 * a - 150) * (5 * b - 150))

def calc_line(y, a, b):
    array = []
    if y == 60:
        for i in range(10, 60, 10):
            array.append(prob(i, 10, a, b) + prob(i, 20, a, b) + prob(i, 30, a, b) + prob(i, 40, a, b) + prob(i, 50, a, b))
    else:
        for i in range(10, 60, 10):
            array.append(prob(i, y, a, b))
    return array

def variance(a, array):
    res = 0
    for i in range(10, 60, 10):
        res += pow(i, 2) * ((a - i) / ((5 * a) - 150))
    return (res - (array ** 2))

def get_array_res(a, b):
    array = []
    for y in range(10, 70, 10):
        array.append(calc_line(y, a, b))
    return (array)

def get_result_y_law(array):
    result_y_law = []
    i = 0
    for y in range(10, 70, 10):
        if y == 60 :
            result_y_law.append(1.000)
        else :
            result_y_law.append(array[i][0] + array[i][1] + array[i][2] + array[i][3] + array[i][4])
        i += 1
    return (result_y_law)