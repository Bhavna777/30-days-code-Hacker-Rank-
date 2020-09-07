#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    list1 = []
    for i in range(0,n):
        words = input()
    list1.append(words)
    list2 = list1[::-1]
    
    print(list2)
