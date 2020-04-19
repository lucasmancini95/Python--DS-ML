# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 10:09:20 2018

@author: manci
"""
#%%
import numpy as np
from numpy.random import randint as randint

def busqueda_alea(n):
    cota_inf = 1
    cota_sup = 1024
    hallado = False
    n_intentos=0
    while (not hallado):
        n_intentos += 1
        propuesta = randint(cota_inf,cota_sup)
        #print(n_intentos, propuesta, cota_inf, cota_sup)
        if (propuesta == n):
            hallado = True
        elif (propuesta < n):
            cota_inf = propuesta
        else: #en este caso propuesta > n
            cota_sup = propuesta
    return n_intentos

def busqueda_bina(n):
    cota_inf = 1
    cota_sup = 1024
    hallado = False
    n_intentos=0
    while (not hallado):
        n_intentos += 1
        propuesta = (cota_inf + cota_sup) // 2
        #print(n_intentos, propuesta, cota_inf, cota_sup)
        if (propuesta == n):
            hallado = True
        elif (propuesta < n):
            cota_inf = propuesta
        else: #en este caso propuesta > n
            cota_sup = propuesta
    return n_intentos
        
def comparar():
    intentos_alea = []
    intentos_bina = []
        
    for i in range(10000):
        n=182
        intentos_alea.append(busqueda_alea(n))
        intentos_bina.append(busqueda_bina(n))
    
    print("Observar que {0} es menor que {1}".format(np.mean(intentos_bina), np.mean(intentos_alea)))

comparar()
#%%
