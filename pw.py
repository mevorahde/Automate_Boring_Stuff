# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:27:13 2018

@author: Owner
"""

#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv)<2:
    print('Usage: python pow.py[account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account + ' .')