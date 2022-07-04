#!/bin/python3
# Списки / массивы

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    # arr.reverse()

    # if len(arr) > n:
    #     print('more than n')

    arr_reverse = arr[::-1]
    for i in arr_reverse:
        print(i, end=' ')
