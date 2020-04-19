# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 16:06:26 2018

@author: manci
"""

#%%
#A
precios_frutas={}  #diccionario de frutas (keys) con sus precio (attributes)
precios_frutas['banana']=30 #automaticamente crea la key y crea uno de los attributes
precios_frutas['manzana']=10
precios_frutas['naranja']=20
precios_frutas['pera']=30

#B
stock_frutas={'banana':6,'manzana':0,'naranja':32,'pera':15}    #diccionario de frutas (keys) con su stock (attributes)
                                                                #en este caso se crea el dicc ya con keys y attributes
#muestro el diccionario completo
for i in precios_frutas:
    print(i,":",precios_frutas[i])

#Reducir los precios de todo en un 10%, es decir modificar los atributos del diccionario
for i in precios_frutas:
    precios_frutas[i]=precios_frutas[i]*0.9 
    print(i,":",precios_frutas[i])
    

#imprimir el nombre, el precio y el stock
for i in precios_frutas:
    print(i,":\n","precio:",precios_frutas[i],"\n stock:",stock_frutas[i])

#calcular cuanto se ganaria si se vende toda la fruta en stock despues del descuento
total=0
for i in precios_frutas:
    total=total+(precios_frutas[i]*stock_frutas[i])
print(total)   


#%%#

#%%
inventario = {
'cajon': ['libro', 'cordel', 'pelusa'],
'mochila': ['libro', 'comida', 'plata', 'moneda'],
'bolsa': ['cordel', 'piedra', 'comida'],
}

inventario

inventario['mochila']=sorted(inventario['mochila']) #funcion sorted que sirve para ordenar los elementos de una lista
inventario.__setitem__('bolsillo',['pelusa','fosforo usado','moneda']) # metodo de la clase dict que sirve para agregar un elemento, agrego la key y le digo cual van aser los attributos en la lista 
inventario.__delitem__('bolsa') # metodo de la clase dict elimin el key con todos sus attributos (no hay que preocuparse por que quede un dato sin puntero)
inventario['cajon'].reverse() #metodo de la clase list, cambia el orden de los elemento de la lista 

print(inventario)
    


#%%

inventario = {
'cajon': ['libro', 'cordel', 'pelusa'],
'mochila': ['libro', 'comida', 'plata', 'moneda'],
'bolsa': ['cordel', 'piedra', 'comida'],
}

inventario['mochila']=sorted(inventario['mochila']) #funcion sorted que sirve para ordenar los elementos de una lista
inventario.__setitem__('bolsillo',['pelusa','fosforo usado','moneda']) # metodo de la clase dict que sirve para agregar un elemento, agrego la key y le digo cual van aser los attributos en la lista 
inventario.__delitem__('bolsa') # metodo de la clase dict elimin el key con todos sus attributos (no hay que preocuparse por que quede un dato sin puntero)
inventario['cajon'].reverse() # metodo de la clase list, cambia el orden de los elemento de la lista 
inventario #imprimo el inventario

s = set() #creo un nuevo conjunto

for i in inventario: #recorro las keys del dict
    for j in inventario[i]: #recorro los atributos de las keys
        s.add(j) #uso el metodo de set y agrego todos los atrubutos de todas las keys del dicionario
s #imprimo el conjunto, por la definicion de conjunto no va a haber repetidos

#%%