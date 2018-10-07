# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:32:31 2018

@author: Owner
"""
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

