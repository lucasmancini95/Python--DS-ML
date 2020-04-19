
# coding: utf-8

# In[50]:


import pandas as pd
import numpy as np

staff_dic={'Nombres':['Juan','Sandra','Julia'],'Cargo':['Profesor','Investigadora','Directora']} #creo un diccionario
staff_df=pd.DataFrame(staff_dic) #creo un DF a travez de un dicc, (obs, el dicc tiene que ser "cuadrado")
staff_df


# In[51]:


#seteamos los indices con los nombres
staff_df.set_index('Nombres')


# In[32]:


#ahora queremos resetear los indices
staff_df.reset_index(inplace=True)
staff_df


# Merge

# In[43]:


estudiantes_df=pd.DataFrame({'Nombres':['Juan','Miguel','Sandra'],'Escuela':['A','B','C']})
estudiantes_df


# In[54]:


df_mergeado_o=pd.merge(staff_df,estudiantes_df,how='outer',left_on='Nombres',right_on='Nombres')
df_mergeado_o # outter es la union


# In[47]:


df_mergeado_i=pd.merge(staff_df,estudiantes_df,how='inner',left_on='Nombres',right_on='Nombres')
df_mergeado_i #inner es la interseccion


# In[56]:


df_mergeado_l=pd.merge(staff_df,estudiantes_df,how='left',left_on='Nombres',right_on='Nombres')
df_mergeado_l #left es la que pones e


# In[58]:


df_mergeado_r=pd.merge(staff_df,estudiantes_df,how='right',left_on='Nombres',right_on='Nombres')
df_mergeado_r #inner es la interseccion

