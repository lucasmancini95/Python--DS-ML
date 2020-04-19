# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:55:43 2018

@author: lucas mancini
"""
def factorial():
    n=int(input("ingrese el numero al que le quiere aplicar el factorial\n"))
    if(n>0):
        j=1
        for i in range(n,0,-1):
            j=i*j
        print("el factorial de", n, "es" , j)
    elif(n==0):
        print("por definicion el factorial de 0 es 1")
    else:
        print("no es posible calcular el factorial de un numero negativo\n")
