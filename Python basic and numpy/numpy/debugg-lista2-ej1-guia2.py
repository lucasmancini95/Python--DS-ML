# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:51:00 2018

@author: manci
"""

#%%
import numpy as np    

def cuadrados(V):
    """
    esta función toma un array V
    e imprime sus elementos al cuadrado.
    """
    W=V.copy() # el ERROR era copiar W=V, ya que es apuntar los dos punteros al mismo datos
    n=len(V)
    for i in range(n):
        W[i]=V[i]**2
    print("El vector cuadrado: ",W)
    return W
        
        
V=np.linspace(0,5,6)
print("El vector original: ",V)
W=cuadrados(V)
print("El vector original: ",V)
print("El vector cuadrado: ",W)
#%%