#!/usr/bin/python3

from calc import *

def print_tab(array, result_y_law) :
    print("\tX=10", "X=20", "X=30", "X=40", "X=50", "Y law", sep='\t')
    i = 0
    for y in range(10, 70, 10):
        if (y == 60) :
            print("X law", end= "\t", sep = "")
        else :
            print("Y=", y, end= "\t", sep = "")
        print("%.3f"%array[i][0], "%.3f"%array[i][1], "%.3f"%array[i][2], "%.3f"%array[i][3], "%.3f"%array[i][4], "%.3f"%result_y_law[i], sep='\t')
        i += 1

def print_Zarray(array, a, b):
    print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100")
    Zarray = []
    Zarray.append(prob(10, 10, a, b))
    Zarray.append(array[1][0] + array[0][1])
    Zarray.append(array[2][0] + array[1][1] + array[0][2])
    Zarray.append(array[3][0] + array[2][1] + array[1][2] + array[0][3])
    Zarray.append(array[4][0] + array[3][1] + array[2][2] + array[1][3] + array[0][4])
    Zarray.append(array[4][1] + array[3][2] + array[2][3] + array[1][4])
    Zarray.append(array[4][2] + array[3][3] + array[2][4])
    Zarray.append(array[4][3] + array[3][4])
    Zarray.append(array[4][4])
    print("p(Z=z)", "%.3f"%Zarray[0], "%.3f"%Zarray[1], "%.3f"%Zarray[2], "%.3f"%Zarray[3], "%.3f"%Zarray[4], "%.3f"%Zarray[5], "%.3f"%Zarray[6], "%.3f"%Zarray[7], "%.3f"%Zarray[8], sep='\t')
    return (Zarray)

def print_expected_variance(array, result_y_law, Zarray, a, b):
    arrayExp = []
    arrayExp.append(array[5][0] * 10 + array[5][1] * 20 + array[5][2] * 30 + array[5][3] * 40 + array[5][4] * 50)
    arrayExp.append(result_y_law[0] * 10 + result_y_law[1] * 20 + result_y_law[2] * 30 + result_y_law[3] * 40 + result_y_law[4] * 50)
    arrayExp.append(Zarray[0] * 20 + Zarray[1] * 30 + Zarray[2] * 40 + Zarray[3] * 50 + Zarray[4] * 60 + Zarray[5] * 70 + Zarray[6] * 80 + Zarray[7] * 90 + Zarray[8] * 100)
    print("expected value of X:", "%.1f"%arrayExp[0], sep='\t')
    print("variance of X:\t", "%.1f"%variance(a, arrayExp[0]), sep='\t')
    print("expected value of Y:", "%.1f"%arrayExp[1], sep='\t')
    print("variance of Y:\t", "%.1f"%variance(b, arrayExp[1]), sep='\t')
    print("expected value of Z:", "%.1f"%arrayExp[2], sep='\t')
    print("variance of Z:\t", "%.1f"%(variance(a, arrayExp[0]) + variance(b, arrayExp[1])), sep='\t')