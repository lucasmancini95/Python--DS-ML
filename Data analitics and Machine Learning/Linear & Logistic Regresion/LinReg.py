# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 12:38:34 2018

@author: rgrimson
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model

# this is our test set, it's just a straight line with some
# Gaussian noise
plt.cla()
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
sigma=1
x=np.linspace(xmin,xmax,n_samples)

X=np.random.uniform(xmin,xmax,n_samples)
plt.hist(X)
a=np.pi
b=1
obs_error=np.random.normal(0,sigma,n_samples)
plt.hist(obs_error)
Y=a*X+b+obs_error
plt.scatter(X,Y)

X = X[:, np.newaxis]

ols = linear_model.LinearRegression()
ols.fit(X, Y)
print(ols.coef_)
print(ols.intercept_)
plt.figure(1)
plt.clf()
plt.scatter(X,Y)
plt.plot(x, ols.coef_ * x + ols.intercept_, linewidth=1,color='r')

plt.ylabel('Y')
plt.xlabel('X')
plt.legend(('Modelo de Regresión Lineal','Observaciones'),
           loc="lower right", fontsize='small')
plt.show()

#%% Análisis de residuos
e=Y-(ols.coef_ * X.ravel() + ols.intercept_)
plt.figure(2)
plt.clf()
plt.hist(e)
plt.title('Histograma de residuos')
plt.figure(3)
plt.clf()
plt.scatter(X,e)
plt.title('Residuos')

