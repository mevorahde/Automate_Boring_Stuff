# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:31:34 2018

@author: David E
"""

def spam(divideBy):
    return 42/ divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')