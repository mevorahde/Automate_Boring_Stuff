# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:01:34 2018

@author: David E
"""

while True: 
    print(' Enter your age:') 
    age = input() 
    if age.isdecimal(): 
        break 
    print(' Please enter a number for your age.') 
while True: 
        print(' Select a new password (letters and numbers only):') 
        password = input() 
        if password.isalnum(): 
            break 
        print(' Passwords can only have letters and numbers.')

