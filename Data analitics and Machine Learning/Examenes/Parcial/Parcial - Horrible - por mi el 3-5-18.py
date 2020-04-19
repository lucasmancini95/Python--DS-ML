# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:05:03 2018

@author: manci
"""
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%

#Ejercicio 1:
df_titanic = pd.read_csv("~/Downloads/Titanic.csv",  encoding = "ISO-8859-1")

#%%
#a)
df_titanic.head(10) #inspecciono los primeros registros
df_titanic[1290:] # inspecciono los ultimos
#%%
#b)
#cada columna de un DataFrame de pandas es un objeto "SERIES"
df_titanic.columns # me dice todas las columnas que tengo
df_titanic.columns.size #tengo 12 columnas

for i in range(0,df_titanic.columns.size): 
    print("La columna: ",df_titanic.columns[i],"tiene datos de tipo:\n",type(df_titanic.iloc[4,i]))
    


#%%
#c)

print(np.where(np.isnan(df_titanic['PassengerId'])))

print(np.where(np.isnan(df_titanic['Survived'])))

print(np.where(np.isnan(df_titanic['Pclass'])))

print(np.where(np.isnan(df_titanic['Age'])))

print(np.where(np.isnan(df_titanic['SibSp'])))

print(np.where(np.isnan(df_titanic['Parch'])))

print(np.where(np.isnan(df_titanic['Fare'])))

print(np.where(np.isnan(df_titanic['Cabin'])))

#con el codigo anterior puedo ver que las siguientes columnas tienen Nan:
    #Age : tiene 262 faltantes
    #Cabin 


#%%

#Ejercicio 2

#%%
    
#a)
    
 #En total habia 843 hombre y 466 mujeres 
df_survived_sex = pd.DataFrame(df_titanic[df_titanic['Survived']==1]) 
df_survived_sex =df_survived_sex[['Sex']]
df_survived_sex[df_survived_sex['Sex']=='male'].size # tengo 109 sobrevivientes hombres
df_survived_sex[df_survived_sex['Sex']=='female'].size # tengo 385 sobrevivientes mujeres

df_not_survived_sex = pd.DataFrame(df_titanic[df_titanic['Survived']==0]) 
df_not_survived_sex =df_not_survived_sex[['Sex']]
df_not_survived_sex[df_not_survived_sex['Sex']=='male'].size # tengo 734 muertos hombres
df_not_survived_sex[df_not_survived_sex['Sex']=='female'].size # tengo 81 muertos mujeres


#%%    
df_hombres=pd.DataFrame()
df_hombres['Sobrevivientes']=[109]
df_hombres['muertos']=[734]
df_mujeres=pd.DataFrame()
df_mujeres['Sobrevivientes']=[385]
df_mujeres['muertos']=[81]

plt.scatter(df_hombres,df_mujeres)
#%%


#%%

#5)

df_titanic.Name.values[0]
aux=[x.split(', ')[1]  for x in df_titanic.Name.values]
titulos=[x.split('.')[0]  for x in aux]
#a)
titulos.count('Rev') # hay 8 reverendos en el barco

#%%

#b)
b= np.where(np.isnan(df_titanic['Age']))[0] # las personas que no tienen dato de edad

for x in b:
    print(titulos[x])

#%%














