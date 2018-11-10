# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 18:11:58 2018

@author: Owner
"""
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <=2:
        raise Exception('Height must be greater than 2.')
        print (symbol * width)
        for i in range(height - 2):
            print(symbol + (' ' * (width - 2)) + symbol)
        
    for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
       try:
           boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happen: ' + str(err))
