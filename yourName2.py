# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:41:19 2018

@author: Owner
"""

name = ''
while name != 'your name':
    print("Please type your name.")
    name = input()
    if name == 'your name':
        break
print("Thank you!")