# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 17:42:52 2018

@author: Owner
"""

brithdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol':'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in brithdays:
        print(brithdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        brithdays[name] = bday
        print ('Birthday database updated.')