# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:26:34 2023

@author: Admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Datasets/animal_category.csv.xls")
df.shape
df.drop(['Index'],axis=1,inplace=True)
df
#check df again
df_new=pd.get_dummies(df)
df_new.shape
#Here we are getting 30 rows and 14 col
#we are getting two col for homely and gender one col
#Delect seocnd column of gender and seocnd col of homely
df_new.drop(['Gender_Male','Homly_Yes'],axis=1,inplace=True)
df_new.shape
#Now we are getting 30,12
df_new.rename(columns={'Gender_Female':'Gender','Homly_No':'Homely'},inplace=True)




#######################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Datasets/ethnic diversity.csv")

df.shape

df.drop(['Sex'],axis=1,inplace=True)
df

df_new=pd.get_dummies(df)
df_new.shape

df_new.drop(['Sex_M','MaritalDesc_Divorced'],axis=1,inplace=True)
df_new.shape
