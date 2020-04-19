# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:14:04 2018

@author: manci
"""

def juego_adivinar_numero():
    respuesta= np.random.randint(1,11)
    
    n=int(input("adivine el numero entre 1 y 10\n"))
    
    while(n!=respuesta):
        if(n>respuesta):
            print("la respuesta es mas chica")
        elif(n<respuesta):
            print("las respuesta en mas grande")
        n=int(input("pruebe otra vez, adivine el numero entre 1 y 10\n"))
    
    
    
    print("felicitaciones!! el numero es", n)