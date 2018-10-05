# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:22:03 2018

@author: David E
"""

def spam():
    global eggs
    eggs = 'spam'

eggs = 'gobal'    
spam()
print(eggs)
    

    