# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:55:43 2018

@author: lucas mancini
"""

def convert_F(num):
    print((num-32)*(5/9))
def convert_C(num2): 
    print(num2*(9/5)+32)
    
def conv_temp():
    data_in=input("ingrese la temperatura que quiere convertir\n")
    
    if(data_in.find('F')!=-1 or data_in.find('C')!=-1 ):
        print("ok")
        if(data_in.find('F')!=-1):
         convert_F(float(data_in[:-1]))
        else:
         convert_C(float(data_in[:-1]))  
    else: print("error")