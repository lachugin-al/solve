#!/bin/python3
# Двоичные числа

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    maximum = 0
    result = 0

    while n > 0:
        s = '1'
        if n % 2 == 1:  # получаем число в двоичной системе
            result += 1
            # print(n%2, end='')
            if result > maximum:
                maximum = result
        else:
            # print(n%2, end='')
            result = 0  # ведем счет до следующего 0

        n //= 2  # делим без остатка для получения следующего числа

print(maximum)
