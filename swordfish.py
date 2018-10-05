# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:47:03 2018

@author: Owner
"""

while True:
    print("Who are you?")
    name = input()
    if name != 'Joe':
        continue
    print("Hello, Joe. What is the password? (It is a fish.)")
    password = input()
    if password == 'swordfish':
        break
print("Access granted.")