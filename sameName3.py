# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:27:16 2018

@author: David E
"""

def spam():
    global eggs
    eggs = 'spam' # this is the global
    
def bacon():
    eggs = 'bacon' # this is a local
def ham():
    print(eggs) #this is the global

eggs = 42 # this is the global
spam()
print(eggs)