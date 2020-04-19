# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 13:51:17 2018

@author: rgrimson
"""
#http://www.fao.org/faostat/es/#data/QC

import pandas as pd
import numpy as np

#%%
df = pd.read_csv("~/Downloads/Production_Crops_E_All_Data.csv",  encoding = "ISO-8859-1")
#%%

df.info()


#%%

df.columns # me muestra todas los tipos de columnas que tengo 

Items=df['Item'].unique() #me crea un ndarray con todas las cadenas que hay en la columna Items
                        #unique es un metodo de la clase series
#%%

Tomatoes_bool=(df['Item']=='Tomatoes') # me crea una Series con valores booleanos
                                  #c/ booleano me dice si el elemento era un tomatoe o no
np.where(Tomatoes_bool)# te devuleve las pocisiones de los True al entregarle un arreglo con booleanos
df_Tomatoes = df[Tomatoes_bool]# ahora el DF tomatoes va a tener los lugares donde esten los trues en el arreglo de booleanos 

# ahora hago lo mismo con argentina

Argentina_bool=(df['Area']=='Argentina')
df_Argentina = df[Argentina_bool]

#%%

dg = df[Tomatoes_bool & Argentina_bool] #dg (un DF) va a tener las filas donde:
                                        #argentina sea True Y donde tomatoes sea true en simultaneo
#si pongo una | en vez del & ---> me va a poner donde tomatoes sea true o argentina sea true
year_cols=['Y'+str(y) for y in np.arange(1961,2017)]
#creo un arreglo con string de la forma YXXXX siendo xxxx los años entre 1961 y 2016
#%%
dg[year_cols]# me va a tirar las columnas desde 1961 hasta la 2016, cree este arreglo porque el DF esta
#indexado segun los años en el formato YXXX (son 3 filas y 56 columnas)
dg[year_cols].T #transpongo
df_ARG_Tom = dg[year_cols].T # se lo asingo a un nuevo DF
df_ARG_Tom.columns=['Superficie','Rinde','Producción'] # le pongo nombre a las 3 columnas del DF
df_ARG_Tom.head() #muestro las primeras 5 filas del DF

#%%

df_ARG_Tom['Superficie'].plot() #polteo bien basico, SUPERFICIE VS el INDEX
#obs importante: hace columna vs el numero de index, no contra el valor

#%%

df_ARG_Tom.plot() #lo mismo pero plotea las 3 columnas vs el index

#%% Ejercicio 1) Plotear la produccion de soja desde 1961 hasta 2016 de los 10 paises que mas produjeron en el periodo

# Armar un df df_soy_prod que tenga solo las filas de df con 'Element'=='Production' & 'Item'=='Soybeans'

df_soy_prod=df[(df['Element']=='Production') &  (df['Item']=='Soybeans')]

# Cuales son las columnas de este nuevo df?

df_soy_prod.columns

#Observar que las primeras 110 filas corresponden a datos de paises y las siguientes ade regiones.
#Seleccionar solo las primeras 110 filas, correspondientes a paises

df_soy_prod=df_soy_prod.iloc[0:110:1]
df_soy_prod=df_soy_prod[['Area']+year_cols] 


#Observar que tiene las series de produccion por pais en las filas y no en las columnas
# => trasponerlo y guardarlo en df_soy_prod_country

df_soy_prod_country= df_soy_prod.T


#mirar el head de este nuevo df y observar que la primera fila tiene los nombres de los paises
#modificar la situacion borrando esta fila y poniendo los nombres como nombres de las columnas

paises=df_soy_prod_country.loc['Area'].values
df_soy_prod_country=df_soy_prod_country.iloc[1:]
df_soy_prod_country.columns=paises

#sugerencias:
# 1.guardar una lista de los paises
#   paises=df_soy_prod_country.loc['Area'].values
# 2.tirar la primera fila con df_soy_prod_country.iloc[1:]
# 3. redefinir los nombres de las columnas 

 #me los ordena de mayor a menor segun  la suma de su produccion
df_10_mayor_produccion=df_soy_prod_country.sum().sort_values(ascending=False)[0:10:1]
paises_10=df_10_mayor_produccion.index
df_soy_prod_country[paises_10].plot()

#cual fue el producto cuyo rendimiento mas aumento en cada decada?


