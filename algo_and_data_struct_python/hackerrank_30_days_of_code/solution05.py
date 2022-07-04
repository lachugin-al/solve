#!/bin/python3
# Циклы

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    for i in range(1, 10 + 1):
        print(f'{n} x {i} = {n*i}')
