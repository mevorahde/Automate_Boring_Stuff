# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:47:55 2018

@author: Owner
"""

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

print("What would you like to ask the magical 8-ball?")    
question = input()
r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)