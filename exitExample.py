# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:18:36 2018

@author: Owner
"""

import sys

while True:
    print("Type exit to exit.")
    response = input()
    if response == 'exit':
        sys.exit()
    print("You typed " + response + " .")