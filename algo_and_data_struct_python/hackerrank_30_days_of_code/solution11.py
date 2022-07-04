#!/bin/python3
# Матрицы / двухмерные массивы

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # arr2 = [1,2,3]
    # print(sum(arr2[0:3]))

    # arr = [[1, 0, 1, 1, 2, 3],
    #        [0, 1, 1, 1, 2, 3],
    #        [0, 0, 0, 1, 2, 3],
    #        [7, 8, 9, 1, 2, 3],
    #        [7, 8, 9, 1, 2, 3],
    #        [7, 8, 9, 1, 2, 3]]
    # print(sum(arr[0][0:3]))

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


def print_sum_matrix_el2(arr):
    maximum = -9 * 9

    for i in range(4):              # смещение на 4 матрицы 3*3 вправо
        for el_in_i in range(4):    # смещение на 4 матрицы 3*3 вниз
            f1 = sum(arr[i][el_in_i:el_in_i + 3])
            f2 = arr[i + 1][el_in_i + 1]
            f3 = sum(arr[i + 2][el_in_i:el_in_i + 3])
            summa = f1 + f2 + f3

            maximum = max(maximum, summa)
    return maximum


print_sum_matrix_el2(arr)
print(print_sum_matrix_el2(arr))

"""def print_matrix_el(arr):
    summa = 0
    for el in arr:
        for element_in in el:
            print(element_in, end=' ')
            summa += element_in
        print(summa, end=' ')
        summa = 0
        print()
print_matrix_el(arr)"""
