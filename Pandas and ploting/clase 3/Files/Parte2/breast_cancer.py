# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)



#%%

# here we will import the libraries 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv), data manipulation as in SQL
import matplotlib.pyplot as plt # this is used for the plot the graph 
import seaborn as sns # used for plot interactive graph. I like it most for plot



#%%

data = pd.read_csv("C:\\Users\\manci\\Desktop\\Materias Actuales\\Curso Analisis de Datos con Python\\Notas y ejercicios para la clase\\clase 3/breast-cancer.csv")# here header 0 means the 0 th row is our coloumn 
                                                # header in data
data.head()

#%%

#check the data
data.head(3)
data.drop("Unnamed: 32",axis=1,inplace=True)
id=data['id']
data.drop("id",axis=1,inplace=True)


#%%
data['diagnosis'].unique()


#%%
#Some basic plots
data.boxplot('radius_mean')
#%%
data.boxplot('radius_mean', by='diagnosis')
#%%
data.plot.scatter('radius_mean','area_mean')

X=np.linspace(0,30,300)
Y=X**3
plt.plot(X,Y,c='r')

#%%
#Now with Seaborn

#%%
#Data analysis

sns.countplot(x='diagnosis',data=data)


#%%

sns.boxplot(x='radius_mean',y='diagnosis',data=data)


#%%

data.info()


#%%

data.columns # this gives the column name which are persent in our data no Unnamed: 32 is not now there


#%%

# As I said above the data can be divided into three parts.lets divied the features according to their category
features_mean= list(data.columns[1:11])
features_se= list(data.columns[11:20])
features_worst=list(data.columns[21:31])
print(features_mean)
print("-----------------------------------")
print(features_se)
print("------------------------------------")
print(features_worst)


#%%

data.describe()


#%%

#check data count
data.count()


#%%

#hot encoding
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
data['diagnosis']=le.fit_transform(data['diagnosis'])
data['diagnosis'].head(5)


#%%

#See the data

data.head(5)


#%%

#Explore the data

sns.countplot(x='diagnosis',data=data)


#%%

data_mean=data[features_mean]
data_mean['diagnosis']=data['diagnosis']
data_mean.head(3)


#%%

#check the details data for the mean feature
plt.figure(figsize=(14,14))
sns.pairplot(data_mean,hue='diagnosis')


#%%

data_mean.columns


#%%

corr=data_mean.corr()
corr = (corr)
plt.figure(figsize=(14,14))
sns.heatmap(corr, cbar = True,  square = True, annot=True, fmt= '.2f',annot_kws={'size': 15},
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
sns.plt.title('Heatmap of Correlation Matrix')
corr


#%%
#
# Ejercicios Parte 2
#
# BREAST
#      1. Ajustar a mano una parábola que ajuste 'area_mean' en función de 'radius_mean' y plotearla justo al scatterplot.
#
#
# TIPS.CSV
#      1. Realizar el boxplots de propina separando si es cena o el almuerzo.
#      2. Plotear total_bill vs. tips. ¿Qué se observa?
#      3. Realizar un histograma del porcentaje de propina sobre el total de la cuenta. ¿Cual es el porcentaje más usual?
#      4. Hacer el scatterplot de tips vs. bill separado por género y tabaquismo.
#%%
#BREAST
#      1. Ajustar a mano una parábola que ajuste 'area_mean' en función de 'radius_mean' y plotearla justo al scatterplot.
data.plot.scatter('radius_mean','area_mean')

X=np.linspace(0,30,300)
Y=3*X**2+4*X
plt.plot(X,Y,c='r')

#%%
# TIPS.CSV
#      1. Realizar el boxplots de propina separando si es cena o el almuerzo.
#      2. Plotear total_bill vs. tips. ¿Qué se observa?
#      3. Realizar un histograma del porcentaje de propina sobre el total de la cuenta. ¿Cual es el porcentaje más usual?
#      4. Hacer el scatterplot de tips vs. bill separado por género y tabaquismo.

#1:
tips_data = pd.read_csv("C:\\Users\\manci\\Desktop\\Materias Actuales\\Curso Analisis de Datos con Python\\Notas y ejercicios para la clase\\clase 3/tips.csv")
tips_data
sns.boxplot(x='tip',y='time',data=tips_data)
tips_data.boxplot('tip',by='time')

#%%
#2:
plt.plot(tips_data.total_bill,tips_data.tip,c='g')

tips_data.plot('total_bill','tip')

#%%

sns.countplot(x=tips_data.tip/tips_data.total_bill,data=tips_data)




#%%