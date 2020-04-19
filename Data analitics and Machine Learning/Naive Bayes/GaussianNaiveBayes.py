#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:05:37 2018

@author: rgrimson
"""

#Esta parte es como la de la clase pasada
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neighbors = 15

# import some data to play with
iris = datasets.load_iris()

# we only take the first two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = iris.data[:, :2]
t = iris.target

h = .02  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
cols=['#FF0000', '#00FF00', '#0000FF']

# we create an instance of Neighbours Classifier and fit the data.
clf = neighbors.KNeighborsClassifier(n_neighbors)
clf.fit(X, t)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)

#%%

#Definimos unas funciones para plotear círculos y elipses

def circle(x, y, radius=0.15,color='black'):
    from matplotlib.patches import Circle
    from matplotlib.patheffects import withStroke
    circle = Circle((x, y), radius, clip_on=False, zorder=10, linewidth=1,
                    edgecolor=color, facecolor=(0, 0, 0, .0125))#,
                    #path_effects=[withStroke(linewidth=5, foreground='w')])

    ax.add_artist(circle)

def ellipse(x, y, width, height, angle=0):
    from matplotlib.patches import Ellipse
    from matplotlib.patheffects import withStroke
    ell =  Ellipse((x, y), width, height, clip_on=False, fill=False, linewidth=1, angle=angle)#, linewidth=2, fill=False, zorder=2)
    ax.add_artist(ell)


#%%
#Ajustamos un modelos gaussiano con naive Bayes

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(iris.data, iris.target)


#si lo usamos como predictor, el modelo anda bien sobre los mismos datos
y_pred = gnb.predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d"
      % (iris.data.shape[0],(iris.target != y_pred).sum()))


#%%
#comparemos en una misma imágen ambos métodos.

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect=1)
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=t, cmap=cmap_bold,
            edgecolor='k', s=20)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
#plt.title("3-Class classification (k = %i)"
#          % (n_neighbors))

#%
for i in range(gnb.theta_.shape[0]):
    theta=gnb.theta_[i]
    sigma=np.sqrt(gnb.sigma_[i])
    x=theta[0]
    y=theta[1]
    width=sigma[0]*2
    height=sigma[1]*2
    #print(x,y,width,height)
    ellipse(x,y,width,height)

#for i in range(150):
#    if (iris.target[i] != y_pred[i]):
#        print(i)
#        x=iris.data[i][0]
#        y=iris.data[i][1]
#        circle(x,y,.1,cols[y_pred[i]])
#        circle(x,y,.07,cols[t[i]])
        
        


