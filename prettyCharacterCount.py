# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 20:47:27 2018

@author: Owner
"""
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)


