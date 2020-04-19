#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
Linear Regression Example
=========================================================
This example uses the only the first feature of the `diabetes` dataset, in
order to illustrate a two-dimensional plot of this regression technique. The
straight line can be seen in the plot, showing how linear regression attempts
to draw a straight line that will best minimize the residual sum of squares
between the observed responses in the dataset, and the responses predicted by
the linear approximation.

The coefficients, the residual sum of squares and the variance score are also
calculated.

"""
#%%
print(__doc__)


# Code source: Jaques Grobler
# License: BSD 3 clause


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

                                
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20] #agarro todo menos los ultimos 20 => 422x10
diabetes_X_test = diabetes_X[-20:]  #agarro solo los ultimos 20 => 20x10

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20] #ahora diabetes_y_train es un arreglo de 422 de largo
diabetes_y_test = diabetes.target[-20:] #ahora diabetes_y_test es un arreglo de 20 de largo
                                #estaba bajo la clave target en el diccionario diabetes original

# Create linear regression object
regr = linear_model.LinearRegression()



# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
#%%

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data[:]  #ahora diabetes_X es un arreglo de 442x10
                                #estaba bajo la clave data en el diccionario diabetes original
                                
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20] #agarro todo menos los ultimos 20 => 422x10
diabetes_X_test = diabetes_X[-20:]  #agarro solo los ultimos 20 => 20x10

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20] #ahora diabetes_y_train es un arreglo de 422 de largo
diabetes_y_test = diabetes.target[-20:] #ahora diabetes_y_test es un arreglo de 20 de largo
                                #estaba bajo la clave target en el diccionario diabetes original

# Create linear regression object
regr = linear_model.LinearRegression()



# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)
#%%