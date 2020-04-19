# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:14:59 2018

@author: rgrimson
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%%
#Podemos levantar los datos normalmente
df = pd.read_csv("sfba_2014_04.csv",index_col='Time')# abre un df y indexa con la columna time
#y las fechas son cadenas
df.index[0]
df.plot()   
#%%

#%%

#o podemos levantarlas como fechas
df = pd.read_csv("sfba_2014_04.csv",parse_dates=['Time'],index_col='Time')
#y tratar a las fechas como un tipo especial
df.index[0]

df.plot()   # al graficar me va a tratar a la columna con una fecha, osea que me grafica teniendo en cuenta los meses, dias ,etc

#%%

plt.clf()

df.SF['2014-04-10':'2014-04-14'].plot()
df.BA['2014-04-10':'2014-04-14'].plot()

#%%
plt.clf()
df['2014-04-18':'2014-04-22'].plot() # ploteo ingresando los dias en un formato de fechas

df['2014-04-19 12':'2014-04-20 15'].plot() # ploteo ingresando los dias en otro formato

#%%
plt.clf()
df.fillna(0)['2014-04-19 12':'2014-04-20 15'].plot()
df.fillna(0)['2014-04-19 12':'2014-04-20 15'].plot() # lo lleno con 0s, pero eso no es real, no sirve

#%%
df['2014-04-20'].mean() # hago el promedio y no tiene en cuenta los NaN
df.fillna(0)['2014-04-20'].mean() #rellena lo NaN con 0 y despues hace el promedio --> esta mal

#%%

df['2014-04-20']
df['2014-04-20'].dropna() #me saca todos lo NaN

#%%

#RESAMPLE resampleo a 10min e interpolo
dg=df['2014-04-21'].resample('10min') #arma otro data frame pero con datos cada 10 min

#%%

#al interpolar lo que va a hacer es completar los Nans  (osea los datos faltantes)
dg.interpolate(method='linear').plot()
dg.interpolate(method='quadratic').plot()
dg.interpolate(method='cubic').plot()
dg=dg.interpolate(method='cubic') #esta es la mejor interpolacion para este caso
                                            #al decirle inplace le digo que modifique el archivo original
SF=dg.SF
BA=dg.BA
dg
#%%

#%%
plt.clf()
plt.plot(BA)
plt.plot(SF)
#%%
plt.clf()
shifts=np.arange(-5,16)
plt.plot(shifts,[SF.corr(BA.shift(t)) for t in shifts])

[SF.corr(BA.shift(t)) for t in shifts]
#%%
plt.clf()
plt.plot(BA.shift(5))
plt.plot(SF)
#%%


###general
pd.to_datetime('2010/11/12', format='%Y/%m/%d')
pd.to_datetime('2010/11/12', format='%Y/%d/%m')
pd.to_datetime('10/11/12', format='%y/%d/%m')

from datetime import datetime
start = datetime(2018, 4, 1)
end = datetime(2018, 4, 30)
pd.date_range(start, end)
pd.date_range(start, end, freq='2D')
pd.date_range(start, end, freq='W')
pd.date_range(start, end, freq='12H')

pd.date_range(start, periods=12, freq='15Min')


#%%
"""Ejercicio:
    
1) usar np.where(np.isnan(df)) para hallar todos los NaNs del dataframe.
2) hallar el shift que maximiza la correlación, considerando múltiplos de 5 minutos y los datos completos.
3) usar los datos de una estación para completar los datos faltantes de la otra, corrigiendo el tiempo según el punto anterior y la altura según corresponda para que se peguen bien.
4) obtener una serie "completada" para San Fernando cada una hora.
"""

#%%

print(np.where(np.isnan(df)))
print(df['SF'][461])# me va a dar el index de la posicion 457
df['BA'][461] # el valor de SF en la fila 457


#%%

dg_5=df.resample('5min') 
dg_5=dg_5.interpolate(method='cubic') #resampleo cada 5 minutos, interpolando cubicamente
#me quedo el archvio df pero con frcuecnia de 5 minutos 

SF_5=dg_5.SF
BA_5=dg_5.BA
#agarro las columnas de BA y de SF que tienen la frecuencia de 5 minutos
shifts=np.arange(-100,100)  
#los shifts van a ser una numeros con los que voya correr SF_5 respecto a BA_5 (cada 5 min obviamente)
plt.plot(shifts,[SF_5.corr(BA_5.shift(t)) for t in shifts]) #ploteo 
correlaciones=[SF_5.corr(BA_5.shift(t)) for t in shifts] # guardo una lista con SF y BA con los distintos corrimientos
shifts[np.argmax(correlaciones)] #me da 11 que es el lugar shifts y el corrimiento
#entonces, lo mejor son 11 shift

BA_5C=BA_5.shift(11)
idx=df.index
idxnan=idx[np.where(df.SF.isna())[0]]
datos=BA_5C.loc[idxnan].values
for n,i in enumerate(idxnan):
    print (n,i)
    df.SF.loc[i]=datos[n]
#%%

nans_SF=np.where(np.isnan(df.SF))
nans_SF = np.array(nans_SF)

aux=df.BA.resample('55min')
aux=aux.interpolate(method='cubic')
df.SF[nans_SF]=aux[nans_SF]


#%%


