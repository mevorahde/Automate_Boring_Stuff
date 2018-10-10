# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 20:46:18 2018

@author: Owner
"""

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

