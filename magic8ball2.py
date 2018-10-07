# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:47:55 2018

@author: Owner
"""

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
print("What would you like to ask the magical 8-ball?")    
question = input()
print(messages[random.randint(0, len(messages) - 1)])

