# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:09:34 2018

@author: manci
"""

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%

df= pd.read_csv("house_prices.csv")

#%%

a= df["totSF"]
len_a=a.shape[0]
a=a.values.reshape(len_a,1)

b= df['SalePrice']
#%%
x_train= a[:-2]
x_test=a[-2:]

y_train= b[:-2]
y_test= b[-2:]

#%%
from sklearn import linear_model

regr=linear_model.LinearRegression()

regr.fit(x_train,y_train)

#%%

y_pred= regr.predict(x_test)
y_pred

#%%
import sklearn.metrics  as sklm

mean_squared_error(y_test,y_pred)
#%%
r2_score(y_test,y_pred)
# OUT:  -299.10276764608363   ---->  da negativo, el modelo es malo pero porque hay un dato que es cualquiera
#%%
plt.scatter(x_train,y_train) # se ve que hay un dato que es negativo, osea que es un absurdo para el precio de una casa
#%%
abline=[regr.coef_ * x + regr.intercept_ for x in x_train]
plt.plot(a,abline)
#%%

#tarea: sacar el valor que es cualquiera y volver a graficar