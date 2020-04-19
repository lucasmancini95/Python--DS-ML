# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 21:25:45 2018

@author: manci
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:55:43 2018

@author: lucas mancini
"""


#%%   
def conv_temp_nparray(data_in,U):
    dim_t=data_in.ndim
    forma=data_in.shape
    dim_1=forma[0]
    if(dim_t==2):
        dim_2=forma[1]
    elif(dim_t>2):
        print("error en dimension")
    if(U=='F'):
        for i in range(0,dim_1,1):
            data_in[i]=(data_in[i]-32)*(5/9)
        if(dim_t>2):
            for j in range(0,dim_2,1):
                data_in[j]=(data_in[j]-32)*(5/9)
         
    elif(U=='C'):
        for i in range(0,dim_1,1):
            data_in[i]=(data_in[i]*(9/5)+32)
        if(dim_t>2):
            for j in range(0,dim_2,1):
                data_in[j]=(data_in[j]*(9/5)+32) 
    else:
        print("error, unidad incorrecta")
    print(data_in)
#%%