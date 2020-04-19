# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:31:58 2018

@author: manci
"""

#%%
def saludar():
 N=[]
 N.append(input("Nombre: "))
 N.append(input("Apellido: "))
 print("Bienvenido {0} {1}!".format(N[0],N[1]))
 return N

saludar()
#%%

def saludar():
 N=[]
 N.append(input("Nombre: "))
 N.append(input("Apellido: "))
 N.append(input("Edad: "))
 print("Bienvenido {0} {1}, de {2} años!".format(N[0],N[1],N[2]))
 return N


saludar()

#%%