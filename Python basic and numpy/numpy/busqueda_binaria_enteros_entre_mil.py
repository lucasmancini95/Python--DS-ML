# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:30:48 2018

@author: manci
"""

#%%

def BB_entre_mil(x):
    limite_izq=1
    limite_der=1024
    estado= False
    
    
    while(estado!=True):
        valor_prop=(limite_izq+limite_der)//2
        if(valor_prop>x):
            limite_der= valor_prop
        elif(valor_prop<x):
            limite_izq= valor_prop
        else:
            estado=True
        print(valor_prop)

 #%%