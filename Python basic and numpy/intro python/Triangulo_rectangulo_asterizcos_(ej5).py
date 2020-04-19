# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:59:43 2018

@author: lucas mancini
"""
def triangulo_rectangulo(base):
    if(type(base)==str):
        print("error")
    else:
        for i in list(range(0,base+1,1)):
            print(i*'*')
