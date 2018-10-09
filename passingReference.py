# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:17:45 2018

@author: David E
"""

def eggs (someParameter):
    someParameter.append('Hello')
    
spam = [1,2,3]
eggs(spam)
print(spam)