#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:45:13 2018
ESTE CODIGO LO DEJO LUCAS BALI CUANDO DIO SU CLASE
@author: lbali
"""

import numpy.random as random
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
#from sklearn.neighbors import NearestNeighbors
from sklearn import neighbors

random.seed(40)
# Da raro con seed = 41...


def generate_data(n):
    x = random.rand(n)*10
    y = 0.5 + 3*x + random.randn(n)*3
    plt.scatter(x,y)
    plt.show()
    return x,y

def generate_data_quad(n):
    x = random.rand(n)*10
    y = 0.5 + 3*x + 0.3*x**2 + random.randn(n)*3
    plt.scatter(x,y)
    plt.show()
    return x,y



def armar_matriz_vandermonde(x, k):
    M = np.zeros((len(x), k+1))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            M[i,j] = x[i]**j
    return M

def ajuste_polinomial(x,y,k):
    M = armar_matriz_vandermonde(x,k)
    #print(M)
    ajustador = linear_model.LinearRegression(fit_intercept=False)
    ajustador.fit(M,y)
    grilla = np.linspace(0,10,num=1000)
    M_grilla = armar_matriz_vandermonde(grilla,k)
    return grilla, ajustador.predict(M_grilla)


def ajuste_polinomial_train_test(x_train,y_train,x_test,degree):
    M = armar_matriz_vandermonde(x_train,degree)
    ajustador = linear_model.LinearRegression(fit_intercept=False)
    ajustador.fit(M,y_train)
    M_test = armar_matriz_vandermonde(x_test,degree)
    return ajustador.predict(M_test)

def armar_folds(n,k):
    bag = np.array(range(n))
    fold_size = int(n/k)
    print("Fold_size: ", fold_size)
    folds = []
    for i in range(k-1):
        fold = random.choice(bag, size = fold_size, replace=False)
        #print("Fold: ", fold)
        #bag = np.delete(bag, fold) # Estaba en el Solvers y era INCORRECTO.
        bag = np.setdiff1d(bag, fold)
        #print("Bag: ", bag)
        folds.append(fold)
    if len(bag) > 0:
        folds.append(bag) # Adjuntamos el remanente del bag.
    return folds


def k_fold_polinomial(x,y, max_degree, k_folds):
    folds = armar_folds(len(x), k_folds)
    errores = []
    bag = range(len(x))
    for degree in range(max_degree+1):
        error = 0.0
        for fold in folds:
            indices_test = fold
            indices_train = np.setdiff1d(bag, fold)
            x_train = x[indices_train]
            x_test = x[indices_test]
            y_train = y[indices_train]
            y_test = y[indices_test]
            y_pred = ajuste_polinomial_train_test(x_train, y_train, x_test, degree)
            error = error + np.mean( (y_test - y_pred)**2)
        errores.append(error)
    return errores



def test_ajuste_polinomial():
     x,y = generate_data(100)
     grilla, values0 = ajuste_polinomial(x,y,0)
     grilla, values1 = ajuste_polinomial(x,y,1)
     grilla, values2 = ajuste_polinomial(x,y,2)
     grilla, values3 = ajuste_polinomial(x,y,3)
     grilla, values4 = ajuste_polinomial(x,y,4)
     plt.scatter(x,y)
     plt.plot(grilla, values0)
     plt.plot(grilla, values1, 'g')
     plt.plot(grilla, values2, 'r')
     plt.plot(grilla, values3, 'c')
     plt.plot(grilla, values4, 'm')
     grilla, values99 = ajuste_polinomial(x,y,99)
     #plt.plot(grilla, values99, 'y')
     plt.show()


def test_folds():
    folds = armar_folds(100,5)
    print(folds)


def test_k_fold():
    x,y = generate_data(100)
    errores = k_fold_polinomial(x,y,10,5)
    print("Errores: ", errores)

def test_LOOCV():
    x,y = generate_data(100)
    errores = k_fold_polinomial(x,y,10,100)
    print("Errores: ", errores)


def test_LOOCV_quad():
    x,y = generate_data_quad(100)
    errores = k_fold_polinomial(x,y,10,100)
    print("Errores: ", errores)



####### CLASIFICACION ############
    
def generate_data_clas():
    n1 = 100
    n2 = 100
    x1 = random.rand(n1)*10
    y1 = random.rand(n1)*20
    x2 = random.rand(n2)*10 + 8
    y2 = random.rand(n2)*20
    plt.scatter(x1,y1)
    plt.scatter(x2, y2)
    plt.show()
    data1 = np.concatenate((np.asmatrix(x1).transpose(), np.asmatrix(y1).transpose()), axis=1)
    data2 = np.concatenate((np.asmatrix(x2).transpose(), np.asmatrix(y2).transpose()), axis=1)
    data = np.concatenate((data1,data2), axis=0)
    z1 = np.zeros((n1,1)) + 0
    z2 = np.zeros((n2,1)) + 1
    z = np.concatenate((z1,z2), axis=0)
    return data,z


def clasificar_knn(data, labels, k):
    clasificador = neighbors.KNeighborsClassifier(k).fit(data,labels)
    return clasificador.predict(np.array((12.0,7.0)).reshape(1,-1))

def CV_class(data, labels):
    folds = armar_folds(data.shape[0],data.shape[0])
    errores = []
    for k in range(1,100):
        error = 0.0
        bag = np.arange(data.shape[0])
        for fold in folds:
            indices_test = fold
            indices_train = np.setdiff1d(bag, fold)
            train_X = data[indices_train,:]
            train_labels = labels[indices_train,:]
            test_X = data[indices_test,:]
            test_labels = labels[indices_test,:]
            clasificador = neighbors.KNeighborsClassifier(k).fit(train_X,train_labels)
            # Predecimos en el test..
            pred = clasificador.predict(test_X)
            error += np.mean(pred!=test_labels)
        errores.append(error / len(folds))
    return errores


def test_CV():
    data, labels = generate_data_clas()
    errores = CV_class(data, labels)
    print("Errores: ", errores)
    plt.plot(range(len(errores)), errores)
    plt.show()


#x,y = generate_data(n=100)
#test_ajuste_polinomial()
#test_folds()   
#test_k_fold()
#test_LOOCV()
#test_LOOCV_quad()

#data, labels = generate_data_clas()
#print(data)
#print(labels)
#print("Predicho como ", clasificar_knn(data, labels, 5))

test_CV()
