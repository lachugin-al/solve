#!/bin/python3
# Рекурсия

import math
import os
import random
import re
import sys


#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    # return 1 if n == 1 else factorial(n - 1) * n
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


if __name__ == '__main__':
    n = int(input())
    print(factorial(n))
    # print(math.factorial(n))