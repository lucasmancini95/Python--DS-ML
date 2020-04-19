# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 13:51:17 2018

@author: rgrimson
"""
#http://www.fao.org/faostat/es/#data/QC

import pandas as pd

#%%
df = pd.read_csv("~/Downloads/Production_Crops_E_All_Data.csv",  encoding = "ISO-8859-1")
#%%

df.info()


#%%

df.columns # t

Items=df['Item'].unique()


#%%

Tomatoes=(df['Item']=='Tomatoes')
np.where(Tomatoes)
df_Tomatoes = df[(df['Item']=='Tomatoes')]

#%%
dg = df[(df['Item']=='Tomatoes') & (df['Area']=='Argentina') ]
year_cols=['Y'+str(y) for y in np.arange(1961,2017)]

#%%
dg[year_cols]
dg[year_cols].T
df_ARG_Tom = dg[year_cols].T
df_ARG_Tom.columns=['Superficie','Rinde','Producción']
df_ARG_Tom.head()

#%%

df_ARG_Tom['Superficie'].plot()

#%%

df_ARG_Tom.plot()

#%% Ejercicio 1) Plotear la produccion de soja desde 1961 hasta 2016 de los 10 paises que mas produjeron en el periodo

# Armar un df df_soy_prod que tenga solo las filas de df con 'Element'=='Production' & 'Item'=='Soybeans'

df_soy_prod = df[(df['Element']=='Production') & (df['Item']=='Soybeans')]

# Cuales son las columnas de este nuevo df?

df_soy_prod.describe()
df_soy_prod.columns

#Observar que las primeras 110 filas corresponden a datos de paises y las siguientes ade regiones.
#Seleccionar solo las primeras 110 filas, correspondientes a paises

#Observar que tiene las series de produccion por pais en las filas y no en las columnas
# => trasponerlo y guardarlo en df_soy_prod_country
df_soy_prod_country = df_soy_prod[['Area']+y_cols].iloc[:110].T

#mirar el head de este nuevo df y observar que la primera fila tiene los nombres de los paises
#modificar la situacion borrando esta fila y poniendo los nombres como nombres de las columnas
df_soy_prod_country.head()


#sugerencias:
# 1.guardar una lista de los paises
#   paises=df_soy_prod_country.loc['Area'].values
# 2.tirar la primera fila con df_soy_prod_country.iloc[1:]
# 3. redefinir los nombres de las columnas 

paises=df_soy_prod_country.loc['Area'].values
df_soy_prod_country = df_soy_prod_country.iloc[1:]
df_soy_prod_country.columns=paises
df_soy_prod_country.plot()

topten=df_soy_prod_country.sum().sort_values(ascending=False)[:10].index

#cual fue el producto cuyo rendimiento mas aumento en cada decada?


