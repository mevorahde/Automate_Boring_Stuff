# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:06:26 2018

@author: David E
"""

def spam():
    eggs = 'Spam local'
    print(eggs) #prints 'spam local'
def bacon():    
    eggs = 'bacon local'
    print(eggs) #prints 'bacon local'
    spam()
    print(eggs) #prints 'bacon local'

eggs = 'gobal'
bacon()
print (eggs) # prints 'global'